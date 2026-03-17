import pandas as pd

def create_time_features(df):

    df['hour'] = df['date_time'].dt.hour
    df['day'] = df['date_time'].dt.day
    df['month'] = df['date_time'].dt.month
    df['weekday'] = df['date_time'].dt.weekday

    df['is_weekend'] = df['weekday'].apply(lambda x: 1 if x >=5 else 0)

    return df


def select_features(df):

    features = [
        'temp',
        'rain_1h',
        'snow_1h',
        'clouds_all',
        'weather_main',
        'weather_description',
        'holiday',
        'hour',
        'day',
        'month',
        'is_weekend'
    ]

    X = df[features]
    y = df['traffic_volume']

    return X, y