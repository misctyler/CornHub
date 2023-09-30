import requests
import time

# Set up variables for the API request
api_url = "https://api.opensea.io/api/v1/assets"
collection_slug = "schizoposters"
trait_type = "Archetype"
trait_value = "TULPAS"

# Define a function to get the current floor price
def get_floor_price():
    # Make the API request
    response = requests.get(api_url, params={
        "order_direction": "desc",
        "offset": "0",
        "limit": "1",
        "collection": collection_slug,
        "asset_contract_address": "0x495f947276749ce646f68ac8c248420045cb7b5e", # OpenSea contract address
        "include_offers": "false",
        "token_ids": "",
        "token_id": "",
        "order_by": "eth_price",
        "traits": f"{trait_type}={trait_value}"
    })

    # Parse the response and return the floor price
    data = response.json()
    if len(data["assets"]) == 0:
        return None
    return data["assets"][0]["sell_orders"][0]["current_price"]

# Continuously monitor the floor price
while True:
    floor_price = get_floor_price()
    if floor_price is None:
        print("No NFTs found with specified trait.")
    else:
        print(f"Current floor price for {trait_value} {trait_type}: {floor_price}")
    time.sleep(60) # Wait 1 minute before checking again
