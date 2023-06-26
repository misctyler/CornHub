from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import json
import os
import pandas as pd

corn_token = Web3.to_checksum_address('0xa0c45509036c422ea7c4d4fcac26a9925531d8c3')
popcorn_token = Web3.to_checksum_address('0x6531547b44784dDD8A934fB9fEB92ba582dfeD15')
butter_token = Web3.to_checksum_address('0x409e02e728418501720d7b1e5d7328ac461ecaae')
w3 = Web3(Web3.HTTPProvider('https://rpc-mainnet.maticvigil.com'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

addresses = [ [Web3.to_checksum_address('0x9bcD90E35A0fCC6aDA241acaBA9A376368B56dF5'),'CornHub'],
              [Web3.to_checksum_address('0x1193d3f5d97e9a8a3B4511a718Eda88C21722B44'),'Factory']]
count = 0
data = []
while count < len(addresses):
    balance_wei = w3.eth.get_balance(addresses[count][0])
    balance_matic = w3.from_wei(balance_wei, 'ether')
    formatted_matic = "{:,.0f}".format(balance_matic)
    row = {'Address': addresses[count][0], 'Name': addresses[count][1], 'Token Balance': formatted_matic, 'Token Ticker' : 'MATIC'}
    data.append(row)

    def check_erc20_bal(x,y):
        with open('/Users/pragma/VIP/CornHub/scripts/ABI_corn.json', 'r') as f: 
            abi = json.load(f)
        ticker = y
        token_contract = w3.eth.contract(address=x, abi=abi)
        balance = token_contract.functions.balanceOf(addresses[count][0]).call()
        decimals = token_contract.functions.decimals().call()
        balance_base_unit = balance / 10 ** decimals
        formatted_balance = "{:,.0f}".format(balance_base_unit)
        row = {'Address': addresses[count][0], 'Name': addresses[count][1], 'Token Balance': formatted_balance, 'Token Ticker': ticker}
        data.append(row)
        
    check_erc20_bal(corn_token, 'CORN')
    check_erc20_bal(popcorn_token,'POPCORN')
    check_erc20_bal(butter_token,'BUTTER')
    count = count + 1
    
df = pd.DataFrame(data)
df = df.drop(df.columns[0], axis=1)
print(df)
