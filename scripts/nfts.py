import os
import requests
import pandas as pd
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()
api_key = os.environ['INFURA_PROJECT_LINK']

w3 = Web3(Web3.HTTPProvider(api_key))
contract_address = Web3.to_checksum_address('0xbfe47d6d4090940d1c7a0066b63d23875e3e2ac5')

token_ids = [
    # ATLANTEANS
    147,2516,752,118,1914,2090,2111,2476,2630,2644,2693,2772,304,3087,
    3110,3496,3627,374,3959,4236,4448,4528,5354,637,819
    # STWABEWWY
    # 1299,1260,53,4755,1594,1883,2322,3266,3669,4863,512,5318,765,
    # #THE GREYS
    # 1626,3679,127,1344,1494,1878,1971,2633,2722,2784,2826,2984,3027,
    # 3038,3157,3268,3887,3950,4098,4239,4309,438,4568,4833,4972,5425,
    # 604,678,746,783,810,811
    ]

abi = '''
[{"inputs":[],"name":"ApprovalCallerNotOwnerNorApproved","type":"error"},
{"inputs":[],"name":"ApprovalQueryForNonexistentToken","type":"error"},
{"inputs":[],"name":"BalanceQueryForZeroAddress","type":"error"},
{"inputs":[],"name":"InvalidQueryRange","type":"error"},
{"inputs":[],"name":"MintERC2309QuantityExceedsLimit","type":"error"},
{"inputs":[],"name":"MintToZeroAddress","type":"error"},
{"inputs":[],"name":"MintZeroQuantity","type":"error"},
{"inputs":[],"name":"OwnerQueryForNonexistentToken","type":"error"},
{"inputs":[],"name":"OwnershipNotInitializedForExtraData","type":"error"},
{"inputs":[],"name":"TransferCallerNotOwnerNorApproved","type":"error"},
{"inputs":[],"name":"TransferFromIncorrectOwner","type":"error"},
{"inputs":[],"name":"TransferToNonERC721ReceiverImplementer","type":"error"},
{"inputs":[],"name":"TransferToZeroAddress","type":"error"},
{"inputs":[],"name":"URIQueryForNonexistentToken","type":"error"},
{"anonymous":false,"inputs":[
    {"indexed":true,"internalType":"address","name":"owner","type":"address"},
    {"indexed":true,"internalType":"address","name":"approved","type":"address"},
    {"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],
    "name":"Approval","type":"event"},
{"anonymous":false,"inputs":[
    {"indexed":true,"internalType":"address","name":"owner","type":"address"},
    {"indexed":true,"internalType":"address","name":"operator","type":"address"},
    {"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],
    "name":"ApprovalForAll","type":"event"},
{"anonymous":false,"inputs":[
    {"indexed":true,"internalType":"uint256","name":"fromTokenId","type":"uint256"},
{"indexed":false,"internalType":"uint256","name":"toTokenId","type":"uint256"},
{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],
"name":"ConsecutiveTransfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],
"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},
{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},
{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint32","name":"quantity","type":"uint32"}],
"name":"SchizoMintedETH","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},
{"indexed":false,"internalType":"uint32","name":"quantity","type":"uint32"}],"name":"SchizoMintedRAD","type":"event"},
{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},
{"indexed":false,"internalType":"uint32","name":"quantity","type":"uint32"}],"name":"SchizoMintedRadlist","type":"event"},
{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"receiver","type":"address"},
{"indexed":false,"internalType":"uint32","name":"quantity","type":"uint32"}],"name":"SchizoMintedReserve","type":"event"},
{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},
{"indexed":true,"internalType":"address","name":"to","type":"address"},
{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},
{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},
{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"}],"name":"WonFreeSchizo","type":"event"},
{"inputs":[],"name":"MAX_SUPPLY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"payable","type":"function"},
{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"beneficiary","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bool","name":"disabled","type":"bool"}],"name":"disableOverlay","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"ethCurve","outputs":[{"internalType":"uint256","name":"lastUpdate","type":"uint256"},{"internalType":"uint128","name":"spotPrice","type":"uint128"},{"internalType":"uint128","name":"priceDelta","type":"uint128"},{"internalType":"uint128","name":"priceDecay","type":"uint128"},{"internalType":"uint128","name":"maxPrice","type":"uint128"},{"internalType":"uint128","name":"minPrice","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"ethMintsEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"explicitOwnershipOf","outputs":[{"components":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"bool","name":"burned","type":"bool"},{"internalType":"uint24","name":"extraData","type":"uint24"}],"internalType":"struct IERC721AUpgradeable.TokenOwnership","name":"ownership","type":"tuple"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"tokenIds","type":"uint256[]"}],"name":"explicitOwnershipsOf","outputs":[{"components":[{"internalType":"address","name":"addr","type":"address"},{"internalType":"uint64","name":"startTimestamp","type":"uint64"},{"internalType":"bool","name":"burned","type":"bool"},{"internalType":"uint24","name":"extraData","type":"uint24"}],"internalType":"struct IERC721AUpgradeable.TokenOwnership[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"numItems","type":"uint256"}],"name":"getPriceETH","outputs":[{"internalType":"uint256","name":"inputValue","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"numItems","type":"uint256"}],"name":"getPriceRAD","outputs":[{"internalType":"uint256","name":"inputValue","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"address","name":"_beneficiary","type":"address"},{"internalType":"address","name":"_randProvider","type":"address"},{"components":[{"internalType":"uint256","name":"lastUpdate","type":"uint256"},{"internalType":"uint128","name":"spotPrice","type":"uint128"},{"internalType":"uint128","name":"priceDelta","type":"uint128"},{"internalType":"uint128","name":"priceDecay","type":"uint128"},{"internalType":"uint128","name":"maxPrice","type":"uint128"},{"internalType":"uint128","name":"minPrice","type":"uint128"}],"internalType":"struct RadLinearCurve.RadCurve","name":"_ethCurve","type":"tuple"},{"components":[{"internalType":"uint256","name":"lastUpdate","type":"uint256"},{"internalType":"uint128","name":"spotPrice","type":"uint128"},{"internalType":"uint128","name":"priceDelta","type":"uint128"},{"internalType":"uint128","name":"priceDecay","type":"uint128"},{"internalType":"uint128","name":"maxPrice","type":"uint128"},{"internalType":"uint128","name":"minPrice","type":"uint128"}],"internalType":"struct RadLinearCurve.RadCurve","name":"_radCurve","type":"tuple"},{"internalType":"string","name":"_withoutOverlayTokenURI","type":"string"},{"internalType":"string","name":"_withOverlayTokenURI","type":"string"},{"components":[{"internalType":"uint256","name":"maxReserveMints","type":"uint256"},{"internalType":"uint256","name":"maxRadlistMints","type":"uint256"},{"internalType":"uint256","name":"maxPrizeMints","type":"uint256"},{"internalType":"uint256","name":"prizePercentChance","type":"uint256"}],"internalType":"struct SchizoPosters.MintParams","name":"_mintParams","type":"tuple"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint32","name":"","type":"uint32"}],"name":"merkleRoots","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"n","type":"uint256"}],"name":"mintFromETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"n","type":"uint256"},{"internalType":"uint256","name":"maxInput","type":"uint256"}],"name":"mintFromRAD","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"n","type":"uint256"}],"name":"mintFromReserve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintParams","outputs":[{"internalType":"uint256","name":"maxReserveMints","type":"uint256"},{"internalType":"uint256","name":"maxRadlistMints","type":"uint256"},{"internalType":"uint256","name":"maxPrizeMints","type":"uint256"},
{"internalType":"uint256","name":"prizePercentChance","type":"uint256"}],"stateMutability":"view","type":"function"},
{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint32","name":"amount","type":"uint32"},{"internalType":"uint32","name":"slots","type":"uint32"},{"internalType":"bytes32[]","name":"radlistProof","type":"bytes32[]"}],"name":"mintRadlist","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"mintedAsPrizes","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintedFromRadlist","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"mintedFromReserve","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"operator","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"overlayDisabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"prizesEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"pullETH","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"radCurve","outputs":[{"internalType":"uint256","name":"lastUpdate","type":"uint256"},{"internalType":"uint128","name":"spotPrice","type":"uint128"},{"internalType":"uint128","name":"priceDelta","type":"uint128"},{"internalType":"uint128","name":"priceDecay","type":"uint128"},{"internalType":"uint128","name":"maxPrice","type":"uint128"},{"internalType":"uint128","name":"minPrice","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"radMintsEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"radcoinV2","outputs":[{"internalType":"contract RadcoinV2","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"radlistMintsClaimed","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"radlistMintsEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"randomness","outputs":[{"internalType":"contract IRandomness","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_beneficiary","type":"address"}],"name":"setBeneficiary","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"lastUpdate","type":"uint256"},{"internalType":"uint128","name":"spotPrice","type":"uint128"},{"internalType":"uint128","name":"priceDelta","type":"uint128"},{"internalType":"uint128","name":"priceDecay","type":"uint128"},{"internalType":"uint128","name":"maxPrice","type":"uint128"},{"internalType":"uint128","name":"minPrice","type":"uint128"}],"internalType":"struct RadLinearCurve.RadCurve","name":"_ethCurve","type":"tuple"}],"name":"setETHCurve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_mintingEnabled","type":"bool"}],"name":"setETHMintingEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_maxPrizeMints","type":"uint32"}],"name":"setMaxPrizeMints","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_maxRadlistMints","type":"uint32"}],"name":"setMaxRadlistMints","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"_maxReserveMints","type":"uint32"}],"name":"setMaxReserveMints","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"key","type":"uint32"},{"internalType":"bytes32","name":"_merkleRoot","type":"bytes32"}],"name":"setMerkleRoot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_operator","type":"address"}],"name":"setOperator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_mintingEnabled","type":"bool"}],"name":"setPrizeMintingEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_prizePercentChance","type":"uint256"}],"name":"setPrizePercentChance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"lastUpdate","type":"uint256"},{"internalType":"uint128","name":"spotPrice","type":"uint128"},{"internalType":"uint128","name":"priceDelta","type":"uint128"},{"internalType":"uint128","name":"priceDecay","type":"uint128"},{"internalType":"uint128","name":"maxPrice","type":"uint128"},{"internalType":"uint128","name":"minPrice","type":"uint128"}],"internalType":"struct RadLinearCurve.RadCurve","name":"_radCurve","type":"tuple"}],"name":"setRADCurve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_mintingEnabled","type":"bool"}],"name":"setRADMintingEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_mintingEnabled","type":"bool"}],"name":"setRadlistMintingEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_randProvider","type":"address"}],"name":"setRandProvider","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_withOverlayTokenURI","type":"string"}],"name":"setWithOverlayTokenURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_withoutOverlayTokenURI","type":"string"}],"name":"setWithoutOverlayTokenURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"tokensOfOwner","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"start","type":"uint256"},{"internalType":"uint256","name":"stop","type":"uint256"}],"name":"tokensOfOwnerIn","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint32","name":"key","type":"uint32"},{"internalType":"uint32","name":"value","type":"uint32"},{"internalType":"address","name":"wallet","type":"address"},{"internalType":"bytes32[]","name":"merkleProof","type":"bytes32[]"}],"name":"verifyMerkleProof","outputs":[{"internalType":"bool","name":"valid","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withOverlayTokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"withoutOverlayTokenURI",
"outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]
'''
contract = w3.eth.contract(address=contract_address, abi=abi)
results_df = pd.DataFrame(columns=['token_id', 'archetype','subtype','holder_address','holder_owned'])
x = 1
while x < 5556:
#for token_id in token_ids:
    token_id = x
    response = requests.get(f'https://schizoposters.xyz/api/tokens/metadata/{token_id}')
    data = response.json()
    subtype_value = ''
    holder_address = contract.functions.ownerOf(token_id).call()
    holder_owned = contract.functions.balanceOf(holder_address).call()
    balance_wei = w3.eth.get_balance(holder_address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    formatted_eth = "{:,.0f}".format(balance_eth)
    for attribute in data['attributes']:
        if attribute['trait_type'] == 'Archetype':
            archetype_value = attribute['value']
        if attribute['trait_type'] == 'Subtype':
            subtype_value = attribute['value']
            break
    print('The holder of ',archetype_value,' ', subtype_value,' ID ', token_id, 'is', holder_address, ' and owns ',holder_owned,' other posters and ',balance_eth,' ETH')
    results_df = results_df.append({
        'token_id': token_id, 
        'archetype': archetype_value, 
        'subtype':subtype_value,
        'holder_address': holder_address, 
        'holder_owned':holder_owned,
        'eth_held':balance_eth}, ignore_index=True)
    x = x + 1

results_df.to_excel('results.xlsx',index=False)