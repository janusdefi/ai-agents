from web3 import Web3

# Connect to an Ethereum node
infura_url = "https://mainnet.infura.io/v3/PROJECTID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is successful
if web3.isConnected():
    print("Connected to Ethereum blockchain")

# Define a smart contract
def load_contract(address, abi):
    contract = web3.eth.contract(address=web3.toChecksumAddress(address), abi=abi)
    return contract

# Example: load an ERC20 token contract
erc20_address = "0xTOKEN_ADDRESS"
erc20_abi = [{
    "constant": true,
    "inputs": [{"name": "account", "type": "address"}],
    "name": "balanceOf",
    "outputs": [{"name": "", "type": "uint256"}],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [
      {"name": "recipient", "type": "address"},
      {"name": "amount", "type": "uint256"}
    ],
    "name": "transfer",
    "outputs": [{"name": "", "type": "bool"}],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "anonymous": false,
    "inputs": [
      {"indexed": true, "name": "from", "type": "address"},
      {"indexed": true, "name": "to", "type": "address"},
      {"indexed": false, "name": "value", "type": "uint256"}
    ],
    "name": "Transfer",
    "type": "event"
  }]

erc20_contract = load_contract(erc20_address, erc20_abi)

# Function to get balance of a wallet
def get_balance(wallet_address):
    return erc20_contract.functions.balanceOf(web3.toChecksumAddress(wallet_address)).call()

# Example usage
wallet_address = "0xWALLET_ADDRESS"
print(f"Wallet balance: {get_balance(wallet_address)} tokens")
