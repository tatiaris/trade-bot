# we need to remove all the tickers that don't exist on robinhood and are priced below $1.5

import requests
from bs4 import BeautifulSoup
import pandas as pd
from stock import Stock
from helper import get_tickers

from constants import ALL_TICKERS_FILEPATH, FILTERED_TICKERS_FILEPATH, MIN_PRICE, MIN_VOLUME

def update_db():
    """ filters tickers based on price and volume and etc """
    tickers = get_tickers(ALL_TICKERS_FILEPATH)
    stocks = []
    new_tickers = []

    for t in tickers:
        try:
            stock = Stock(t)
            if stock.avg_volume > MIN_VOLUME and stock.price > MIN_PRICE:
                stocks.append(stock)
                new_tickers.append(t)
                print(f'Added ${t} to db')
            else:
                print(f'Skipped stock ${t}: avg_vol = ${stock.avg_volume}, price = ${stock.price}')
        except Exception as e:
            print(f'Can\'t find ${t}', e)

    df = pd.DataFrame(new_tickers, columns=['ticker'])
    df.to_csv(FILTERED_TICKERS_FILEPATH, index=False)

if __name__ == '__main__':
    update_db()
