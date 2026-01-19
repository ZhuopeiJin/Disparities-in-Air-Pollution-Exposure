import statsmodels.api as sm
from sklearn.linear_model import LassoCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import xgboost as xgb

def linear_regression(X_train, y_train, X_test, y_test):
    X_train = sm.add_constant(X_train)
    X_test = sm.add_constant(X_test)
    model = sm.OLS(y_train, X_train).fit()
    r2 = model.rsquared
    return model, r2


def lasso_regression(X_train, y_train, X_test, y_test):
    model = LassoCV(alphas=[0.0001,0.001,0.01,0.1,1,10]).fit(X_train, y_train)
    return model, model.score(X_test, y_test)


def random_forest(X_train, y_train, X_test, y_test):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    return model, model.score(X_test, y_test)


def gradient_boosting(X_train, y_train, X_test, y_test):
    model = GradientBoostingRegressor(n_estimators=100, max_depth=1)
    model.fit(X_train, y_train)
    return model, model.score(X_test, y_test)


def xgboost_model(X_train, y_train, X_test, y_test):
    model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=100)
    model.fit(X_train, y_train)
    return model, model.score(X_test, y_test)
