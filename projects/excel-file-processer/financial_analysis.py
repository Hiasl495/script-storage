import pandas as pd
import numpy as np
import requests
import openpyxl


# Replace 'YOUR_API_KEY' with your actual API key from Financial Modeling Prep
API_KEY = 'bff89022d3fad51bfe821bff9618b9a3'
BASE_URL = 'https://financialmodelingprep.com/api/v3/'

symbols = ["AAPL", "MSFT", "KO", "AMZN", "TSLA", "GOOGL"]

list_dfs = []
for symbol in symbols:
    # Financial Statements
    #income_statement_endpoint = f'income-statement/{symbol}?apikey={API_KEY}'
    #balance_sheet_statement_endpoint = f'balance-sheet-statement/{symbol}?apikey={API_KEY}'
    #cash_flow_statement_endpoint = f'cash-flow-statement/{symbol}?apikey={API_KEY}'

    # Financial Analysis (Ratios, KPIs etc.)
    #financial_ratios_ttm_endpoint = f'ratios-ttm/{symbol}?apikey={API_KEY}'
    financial_ratios_endpoint = f'ratios/{symbol}?apikey={API_KEY}'

    # Responses (JSON)
    #response = requests.get(BASE_URL + income_statement_endpoint)
    #response = requests.get(BASE_URL + balance_sheet_statement_endpoint)
    #response = requests.get(BASE_URL + cash_flow_statement_endpoint)
    #response = requests.get(BASE_URL + financial_ratios_ttm_endpoint)
    response = requests.get(BASE_URL + financial_ratios_endpoint)
    json_data = response.json()

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response and create a DataFrame
        data = response.json()
        df_it = pd.DataFrame(data)

        # only for financial ratios
        df_it["symbol"] = symbol

        # Append the DataFrame to the list
        list_dfs.append(df_it)
    else:
        print(f"Error fetching data for symbol {symbol}")

# Concatenate all the dataframes into a single DataFrame
result_df = pd.concat(list_dfs, ignore_index=True)

filename = 'financial_data.xlsx'

result_df.to_excel(filename, index=False, engine='openpyxl')
