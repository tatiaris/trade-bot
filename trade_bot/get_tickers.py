""" read tickers from csv file """


import pandas as pd

from stock import Stock
from constants import ALL_TICKERS_FILEPATH


def get_tickers():
    """ get tickers from csv file """
    df = pd.read_csv(ALL_TICKERS_FILEPATH)

    tickers = df['ticker']

    # remove columns that aren't 'ticker' from csv file
    #tickers.to_csv(ALL_TICKERS_FILEPATH, index=False)

    return tickers


def get_ticker_data():
    """ print the stock data for every ticker """
    tickers = get_tickers()
    stocks = []
    blowing_stocks = []

    for ticker in tickers:
        try:
            stock = Stock(ticker)
            stocks.append(stock)
            print(stock)
            if stock.is_blowing():
                blowing_stocks.append(stock)
            print('Blowing?', 'Y' if stock.is_blowing() else 'N', '\n')
        except Exception as e:
            print(f'Error on ticker {ticker}')
            print(e)
            print()

    print('*' * 40)
    print([stock.ticker for stock in blowing_stocks])


if __name__ == '__main__':
    # print(get_tickers())
    get_ticker_data()
