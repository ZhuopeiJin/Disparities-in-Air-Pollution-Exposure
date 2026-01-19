from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

def build_rf_pipeline(use_pca=False):
    steps = [
        ("scaler", StandardScaler()),
        ("selector", VarianceThreshold())
    ]

    if use_pca:
        steps.append(("pca", PCA(n_components=2)))

    steps.append(("regressor", RandomForestRegressor(random_state=0)))
    return Pipeline(steps)


def tune_random_forest(pipe, X_train, y_train):
    param_grid = {
        "regressor__n_estimators": [100, 500],
        "regressor__max_features": ["sqrt", "log2"],
        "regressor__bootstrap": [True, False]
    }

    grid = GridSearchCV(pipe, param_grid, cv=2)
    grid.fit(X_train, y_train)
    return grid
