# we need to remove all the tickers that don't exist on robinhood and are priced below $1.5

import requests
from bs4 import BeautifulSoup
import pandas as pd

FILEPATH = 'resources/companies.csv'
DB_FILEPATH = 'resources/db.csv'

class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = None
        self.load_data()

    def load_data(self):
        robin_result = requests.get('https://robinhood.com/stocks/' + self.ticker)
        robin_c = robin_result.content
        robin_soup = BeautifulSoup(robin_c, features="html.parser")

        self.price = float(robin_soup.find_all(
            attrs={"class": "QzVHcLdwl2CEuEMpTUFaj"})[0].text.replace(',', '')[1:])

def get_tickers():
    """ get tickers from csv file """
    df = pd.read_csv(FILEPATH)
    tickers = df['ticker']
    return tickers

def update_db():
    """ print the data for every ticker """
    tickers = get_tickers()
    stocks = []

    for ticker in tickers:
        try:
            stock = Stock(ticker)
            if (stock.price > 1.5):
                stocks.append(stock)
                print(f'Added ${ticker} to db')
            else:
                print(f'Skipped penny stock ${ticker} ${ticker.price}')
        except Exception as e:
            print(f'Can\'t find ${ticker}')

    new_tickers = []
    for s in stocks:
        new_tickers.append(s.ticker)
    df = pd.DataFrame(new_tickers, columns=['ticker'])
    print (df)
    df.to_csv('db.csv', index=False)

if __name__ == '__main__':
    update_db()
