import os
import requests
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt

# Load environment variables
load_dotenv()

# Dune API endpoint and headers
API_KEY = os.getenv('DUNE_API_KEY')
BASE_URL = 'https://api.dune.com/api/v1/'
headers = {
    'x-dune-api-key': API_KEY
}

# Query details
query_id = 'YOUR_QUERY_ID_HERE'  # Replace with the actual query ID from Dune

# Function to execute query and get results
def execute_query(query_id):
    # Execute the query
    execute_endpoint = f'{BASE_URL}query/{query_id}/execute'
    response = requests.post(execute_endpoint, headers=headers)
    execution_id = response.json()['execution_id']

    # Get the results
    results_endpoint = f'{BASE_URL}execution/{execution_id}/results'
    while True:
        response = requests.get(results_endpoint, headers=headers)
        if response.json()['state'] == 'QUERY_STATE_COMPLETED':
            return response.json()['result']['rows']

# Execute the query and get results
results = execute_query(query_id)

# Convert results to a pandas DataFrame
df = pd.DataFrame(results)

# Convert 'period' to datetime and set as index
df['period'] = pd.to_datetime(df['period'])
df.set_index('period', inplace=True)

# Create a line plot
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['monthly_gas_spent'], label='Monthly Gas Spent')
plt.plot(df.index, df['cumulative_gas_spent'], label='Cumulative Gas Spent')

plt.title("Vitalik's Gas Spending Over Time")
plt.xlabel('Date')
plt.ylabel('USD')
plt.legend()
plt.grid(True)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()

# Print summary statistics
print(df.describe())
