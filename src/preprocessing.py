import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):

    df = df.copy()

    # Handle missing values
    df.ffill()

    # Encode categorical columns
    categorical_cols = ['weather_main', 'weather_description', 'holiday']

    encoders = {}

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    return df, encoders


def scale_features(X):

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler