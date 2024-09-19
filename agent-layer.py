import numpy as np
import pandas as pd
import asyncio
from web3 import Web3


infura_url = "https://mainnet.infura.io/v3/PROJECTID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check connection
if web3.isConnected():
    print("Connected to Ethereum blockchain")

# Chainlink Oracle Price Feed Contract (e.g., ETH/USD)
oracle_address = "0x5f4ec3df9cbd43714fe2740f5e3616155c5b8419" # This is Chainlink's ETH/USD price feed on Ethereum mainnet

# Oracle ABI (Simplified version for demonstration)
oracle_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "latestRoundData",
        "outputs": [
            {"name": "roundId", "type": "uint80"},
            {"name": "answer", "type": "int256"}, # The price data
            {"name": "startedAt", "type": "uint256"},
            {"name": "updatedAt", "type": "uint256"},
            {"name": "answeredInRound", "type": "uint80"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

class TradingAgent:
    def __init__(self, name, trading_strategy, risk_management):
        self.name = name
        self.trading_strategy = trading_strategy
        self.risk_management = risk_management
    
    def fetch_data(self):
        # Fetch data from a decentralized exchange or oracle (stub function)
        oracle_contract = web3.eth.contract(address=oracle_address, abi=oracle_abi)
        try:
          # Call the latestRoundData function of the oracle
          latest_data = oracle_contract.functions.latestRoundData().call()
          
          round_id, price, started_at, updated_at, answered_in_round = latest_data
          
          # The price is typically returned with 8 decimal places
          price_in_eth = price / (10 ** 8)
          
          return {
              "round_id": round_id,
              "price": price_in_eth,
              "started_at": started_at,
              "updated_at": updated_at,
              "answered_in_round": answered_in_round
          }
        except Exception as e:
          print(f"Error fetching data from oracle: {e}")
          return None
    
    def analyze_data(self, data):
        # Analyze data using your strategy (e.g., technical analysis)
        # Let's assume it's based on simple moving averages
        short_window = 40
        long_window = 100
        signals = pd.DataFrame(index=data.index)
        signals['signal'] = 0.0
        signals['short_mavg'] = data['price'].rolling(window=short_window, min_periods=1).mean()
        signals['long_mavg'] = data['price'].rolling(window=long_window, min_periods=1).mean()
        signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
        return signals

    async def execute_trade(self, signals):
        # Execute trade based on analysis
        for signal in signals.itertuples():
            if signal.signal == 1.0:
                print(f"Buying token at {signal.Index}")
            elif signal.signal == 0.0:
                print(f"Selling token at {signal.Index}")
    
    async def run(self):
        while True:
            data = self.fetch_data()
            signals = self.analyze_data(data)
            await self.execute_trade(signals)
            await asyncio.sleep(10)  # Run the agent every 10 seconds


oracle_data = fetch_price_from_oracle()
if oracle_data:
    print(f"ETH/USD Price: {oracle_data['price']}")
    print(f"Updated at (timestamp): {oracle_data['updated_at']}")

# Perform a simple moving average crossover strategy
def sma_crossover(self):
        df = pd.DataFrame(self.price_data, columns=['price'])
        df['SMA_short'] = df['price'].rolling(window=10).mean()
        df['SMA_long'] = df['price'].rolling(window=30).mean()

        if df['SMA_short'].iloc[-1] > df['SMA_long'].iloc[-1]:
            return "buy"
        elif df['SMA_short'].iloc[-1] < df['SMA_long'].iloc[-1]:
            return "sell"
        else:
            return "hold"

# Risk management strategy (stub)
def risk_management():
    #See risk-management.py
    pass

# Instantiate an agent
agent = TradingAgent(name="Agent1", trading_strategy=sma_crossover, risk_management=risk_management)

# Run the agent
async def main():
    await agent.run()

# Start the asyncio loop
asyncio.run(main())
