import os
from typing import List

# types
Tickers = List[str]

# Resource paths
REPO_FOLDER = os.path.dirname(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(REPO_FOLDER, 'resources')
ALL_TICKERS_FILEPATH = os.path.join(DATA_FOLDER, 'all_tickers.csv')
FILTERED_TICKERS_FILEPATH = os.path.join(DATA_FOLDER, 'filtered_tickers.csv')

MIN_FRACTION_BLOWING = .5  # delete later

# Factors for what stocks to prune out from analysis
MIN_PRICE = 2  # $$$
MIN_VOLUME = 500000

# Threads for performing stock data requests and databasing in parallel
NUM_THREADS = 10
