import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Example of loading and preprocessing big data
def load_and_preprocess_data(file_path):
    # Load data
    df = pd.read_csv(file_path)

    # Feature Engineering: Add features like moving averages, volatility, etc.
    df['ma_7'] = df['price'].rolling(window=7).mean()
    df['ma_30'] = df['price'].rolling(window=30).mean()
    df['volatility'] = df['price'].rolling(window=30).std()

    # Fill missing values
    df.fillna(method='bfill', inplace=True)

    # Scale data
    scaler = MinMaxScaler()
    scaled_df = scaler.fit_transform(df)

    return scaled_df

# Load data
data = load_and_preprocess_data('historical_price_data.csv')
