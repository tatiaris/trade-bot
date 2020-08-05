""" Functions pertaining to read/write from Database """

import threading

from stock import Stock
from get_tickers import get_tickers
from constants import NUM_THREADS, Tickers


def populate_db():
    if True:  # TODO: only populate db if it hasn't been populated before
        tickers = get_tickers()

        # generator of lists of tickers, each ticker in 'tickers' is in 'ticker_lists' once
        ticker_lists = (tickers[i:i + NUM_THREADS]
                        for i in range(0, len(tickers), NUM_THREADS))

        # start threads
        threads = []
        for args in ticker_lists:
            thread = threading.Thread(
                target=_add_stocks_to_db_thread, args=(args,))
            threads.append(thread)
            thread.start()

        # join threads
        for thread in threads:
            thread.join()


def update_db():
    pass


def _add_stocks_to_db_thread(tickers: Tickers) -> None:
    stocks = []
    for ticker in tickers:
        stock = Stock(ticker)
        stocks.append(stock)

    # TODO: add stock to database


def _update_stocks_in_db_thread(tickers: Tickers) -> None:
    pass
