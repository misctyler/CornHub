import requests
wallet_address = "0x9bcD90E35A0fCC6aDA241acaBA9A376368B56dF5"

# URL for Polygon's RPC endpoint
url = "https://rpc-mainnet.maticvigil.com/"

# Get the list of ERC20 token balances for the wallet
def get_erc20_balances():
    balances = {}
    # Request the list of ERC20 token balances using the "eth_call" JSON-RPC method
    for i in range(1, 100):
        response = requests.post(url, json={
            "jsonrpc": "2.0",
            "id": i,
            "method": "eth_call",
            "params": [{
                "to": "0x0000000000000000000000000000000000001010",
                "data": "0xf4adcb1e" + "000000000000000000000000" + wallet_address[2:]
            }, "latest"]
        }).json()
        try:
            # Parse the response to get the token address and balance
            token_address = "0x" + response["result"][26:66]
            balance = int(response["result"][66:], 16)
            # Store the token balance in the dictionary
            if balance > 0:
                balances[token_address] = balance
        except KeyError:
            print("Error: Failed to retrieve ERC20 token balance. Response:", response)
    return balances

# Print out the ERC20 token balances for the wallet
balances = get_erc20_balances()
if len(balances) == 0:
    print("The wallet has no ERC20 token balances.")
else:
    print("ERC20 token balances for wallet", wallet_address, ":")
    for token_address, balance in balances.items():
        try:
            # Request the token symbol using the "eth_call" JSON-RPC method
            response = requests.post(url, json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "eth_call",
                "params": [{
                    "to": token_address,
                    "data": "0x95d89b41"
                }, "latest"]
            }).json()
            # Parse the response to get the token symbol
            symbol = bytes.fromhex(response["result"][2:]).decode()
            print(symbol, "(", token_address, ")", "balance:", balance)
        except KeyError:
            print("Error: Failed to retrieve ERC20 token symbol. Response:", response)
