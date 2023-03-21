from web3 import Web3
import json
import os
print(os.getcwd())

corn_token = '0xa0c45509036c422ea7c4d4fcac26a9925531d8c3'
popcorn_token = '0x6531547b44784dDD8A934fB9fEB92ba582dfeD15'
butter_token = '0x409e02e728418501720d7b1e5d7328ac461ecaae'

w3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.maticvigil.com'))
address = '0x1193d3f5d97e9a8a3B4511a718Eda88C21722B44'
balance_wei = w3.eth.get_balance(address)
balance_matic = w3.from_wei(balance_wei, 'ether')
print(f"Address {address} has a balance of {balance_matic} MATIC")

with open('ABI_corn.json', 'r') as f:
    abi = json.load(f)
token_contract = w3.eth.contract(address=corn_token, abi=abi)
balance = token_contract.functions.balanceOf(address).call()
decimals = token_contract.functions.decimals().call()
balance_base_unit = balance / 10 ** decimals
print(f"Address {address} has a balance of {balance_base_unit} tokens")
