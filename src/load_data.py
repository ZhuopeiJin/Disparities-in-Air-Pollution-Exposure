import pandas as pd
from pathlib import Path

def load_pm25_data(data_dir: Path):
    """Load and combine PM2.5 CSV files."""
    dfs = []
    for i in range(1, 6):
        dfs.append(pd.read_csv(data_dir / f"PM2.5({i}).csv"))
    return pd.concat(dfs, ignore_index=True)


def load_traffic_data(data_dir: Path):
    """Load traffic dataset."""
    return pd.read_csv(data_dir / "traffic.csv")


def load_acs_data(data_dir: Path):
    """Load and combine ACS yearly data."""
    dfs = []
    for year in range(2011, 2022):
        df = pd.read_csv(data_dir / f"ACS {year}.csv")
        df["year"] = year
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)


def load_zcta_state_crosswalk(data_dir: Path):
    """Load ZCTA to state mapping."""
    return pd.read_excel(data_dir / "convert.xlsx")
