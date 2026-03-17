import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from src.preprocessing import scale_features


def train_models(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    X_train_scaled, scaler = scale_features(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Random Forest
    rf = RandomForestRegressor(n_estimators=200, random_state=42)
    rf.fit(X_train_scaled, y_train)

    # Gradient Boosting
    gb = GradientBoostingRegressor()
    gb.fit(X_train_scaled, y_train)

    models = {
        "RandomForest": rf,
        "GradientBoosting": gb
    }

    return models, scaler, X_test_scaled, y_test