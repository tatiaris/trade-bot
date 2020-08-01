# we need to remove all the tickers that don't exist on robinhood and are priced below $1.5

import requests
from bs4 import BeautifulSoup
import pandas as pd

from constants import ALL_TICKERS_FILEPATH, FILTERED_TICKERS_FILEPATH, MIN_PRICE, MIN_VOLUME


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = None
        self.load_data()

    def load_data(self):
        yahoo_result = requests.get("https://finance.yahoo.com/quote/" + self.ticker)
        robin_result = requests.get('https://robinhood.com/stocks/' + self.ticker)

        yahoo_c = yahoo_result.content
        robin_c = robin_result.content

        yahoo_soup = BeautifulSoup(yahoo_c, features="html.parser")
        robin_soup = BeautifulSoup(robin_c, features="html.parser")

        self.price = float(robin_soup.find_all(
            attrs={"class": "QzVHcLdwl2CEuEMpTUFaj"})[0].text.replace(',', '')[1:])
        self.avg_volume = int(yahoo_soup.find_all(
            attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"})[0].text.replace(',', ''))


def get_tickers():
    """ get tickers from csv file """
    df = pd.read_csv(ALL_TICKERS_FILEPATH)
    tickers = df['ticker']
    return tickers


def update_db():
    """ print the data for every ticker """
    tickers = get_tickers()
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
