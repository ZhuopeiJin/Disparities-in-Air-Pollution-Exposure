import pandas as pd

def clean_pm25(df):
    df = df.drop(columns=["Unnamed: 0"], errors="ignore")
    df = df.dropna(subset=["zcta"])
    df["zcta"] = df["zcta"].astype(int)
    return df


def clean_traffic(df):
    drop_cols = [
        'intp_flag','i_min_traffic','i_max_traffic','i_count_traffic',
        'i_min_hw_traffic','i_max_hw_traffic','i_count_hw_traffic',
        'i_min_nonhw_traffic','i_max_nonhw_traffic','i_count_nonhw_traffic'
    ]
    df = df.drop(columns=drop_cols, errors="ignore")
    df = df.rename(columns={"zcta19": "zcta"})
    return df


def clean_acs(df):
    df = df.rename(columns={"ZCTA": "zcta"})
    df = df.dropna()
    df["zcta"] = df["zcta"].astype(int)

    df["Bachelor_or_higher"] = df[
        ["Bachelor", "Master", "prefessional", "doctor"]
    ].sum(axis=1)

    drop_cols = [
        "Bachelor","Master","prefessional","doctor",
        "population25","lessthanhighschool","highschool",
        "college","PovertyStatus","PovertyUnder50"
    ]
    return df.drop(columns=drop_cols, errors="ignore")


def merge_all(pm25, traffic, acs, crosswalk):
    df = pm25.merge(traffic, on=["year", "zcta"])
    df = df.merge(crosswalk[["zcta", "STATE"]], on="zcta", how="left")
    df = df.merge(acs, on=["year", "zcta"], how="left")
    return df.dropna()


def filter_texas(df):
    return df[df["STATE"] == "TX"]
