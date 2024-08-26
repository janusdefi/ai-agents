#Janus AI Agent Price Prediction
#Predict prices of Janus Alpha and Janus Omega Tokens
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import requests
import datetime

# Mock function to get token price from an oracle service
def get_token_price(token_symbol):
    # Simulate an API call to an oracle service
    # For real implementation, integrate with a service like Chainlink
    response = requests.get(f'https://api.mockoracle.com/v1/prices/{token_symbol}')
    if response.status_code == 200:
        return response.json()['price']
    else:
        raise Exception(f"Failed to get token price for {token_symbol}")

# Function to fetch historical token price data (mock data for this example)
def fetch_historical_data(token_symbol):
    dates = pd.date_range(start="2023-01-01", end="2023-12-31")
    prices = np.random.random(size=len(dates)) * 100 # Random data for example
    data = pd.DataFrame({"Date": dates, "Close": prices})
    data['Date'] = data['Date'].map(pd.Timestamp.toordinal)
    return data

# Fetch historical token price data
token_symbol = 'JALPHA'
data = fetch_historical_data(token_symbol)

# Prepare the data
X = data[['Date']]
y = data['Close']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
plt.figure(figsize=(10,5))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted Prices')
plt.xlabel('Date')
plt.ylabel('Token Price')
plt.title('Token Price Prediction')
plt.legend()
plt.show()

# Predict future token price
future_date = datetime.datetime(2024, 1, 1)
future_date_ordinal = np.array([[future_date.toordinal()]])
future_price = model.predict(future_date_ordinal)
print(f"Predicted token price for {future_date.date()}: ${future_price[0]:.2f}")

# Fetch current token price using the oracle service
current_price = get_token_price(token_symbol)
print(f"Current token price for {token_symbol}: ${current_price:.2f}")
