import pandas as pd

def load_data(path):
    """
    Load traffic dataset
    """
    df = pd.read_csv(path)

    # convert date_time to datetime
    df['date_time'] = pd.to_datetime(df['date_time'])

    return df