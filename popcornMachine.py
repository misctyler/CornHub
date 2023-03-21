from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import json
import os

corn_token = Web3.to_checksum_address('0xa0c45509036c422ea7c4d4fcac26a9925531d8c3')
popcorn_token = Web3.to_checksum_address('0x6531547b44784dDD8A934fB9fEB92ba582dfeD15')
butter_token = Web3.to_checksum_address('0x409e02e728418501720d7b1e5d7328ac461ecaae')

w3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.maticvigil.com'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

address = Web3.to_checksum_address('0x1193d3f5d97e9a8a3B4511a718Eda88C21722B44')
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

latest_block = w3.eth.get_block('latest')['number']
address_list = set()
transfer_filter = token_contract.events.Transfer.create_filter(fromBlock=0, toBlock=latest_block)
for event in transfer_filter.get_all_entries():
    if event['args']['to'] == corn_token:
        address_list.add(event['args']['to'])
