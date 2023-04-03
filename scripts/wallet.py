import os
import requests
import networkx as nx
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ['ETHERSCAN_API_KEY']

address = '0x19e02b992c0295d27eecff941d5dbfaf85409d86'

G = nx.DiGraph()
G.add_node(address)
addresses_to_scan = [address]
depth = 0
max_depth = 3
while depth <= max_depth:
    depth += 1
    new_addresses_to_scan = []
    for address in addresses_to_scan:
        url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for tx in data['result']:
                if isinstance(tx, dict):
                    from_address = tx['from']
                    to_address = tx['to']
                    G.add_node(from_address)
                    G.add_edge(from_address, address)
                    if to_address is not None:
                        G.add_node(to_address)
                        G.add_edge(address, to_address)
                        if to_address not in new_addresses_to_scan:
                            new_addresses_to_scan.append(to_address)
        
    addresses_to_scan = new_addresses_to_scan
    if not addresses_to_scan:
        break

# print some information about the graph
print(f'Number of nodes: {G.number_of_nodes()}')
print(f'Number of edges: {G.number_of_edges()}')
print(f'Diameter: {nx.diameter(G)}')
