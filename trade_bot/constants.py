import os
from typing import List

# types
Tickers = List[str]

# Resource paths
REPO_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(REPO_FOLDER, 'data')
ALL_TICKERS_FILEPATH = os.path.join(DATA_FOLDER, 'all_tickers.csv')
FILTERED_TICKERS_FILEPATH = os.path.join(DATA_FOLDER, 'filtered_tickers.csv')
WATCHLIST_TICKERS_FILEPATH = os.path.join(DATA_FOLDER, 'watchlist.csv')

MIN_FRACTION_BLOWING = 2  # delete later

# Factors for what stocks to prune out from analysis
MIN_PRICE = 2  # $$$
MIN_VOLUME = 500000

# ALPACA Config constants
API_KEY = "PKK4RI1CLRVSKATPJK7J"
API_SECRET = "QipDoZBHPloObraVymMmOxSc4VniXmst5wU2ueLn"
BASE_URL = "https://paper-api.alpaca.markets"
ACC_URL = f"{BASE_URL}/v2/account"
ORDERS_URL = f"{BASE_URL}/v2/orders"
POS_URL = f"{BASE_URL}/v2/positions"
BAR_URL = f"{BASE_URL}/v1/bars/1D"
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': API_SECRET}
