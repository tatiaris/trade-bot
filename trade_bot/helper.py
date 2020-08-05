import pandas as pd
from stock import Stock
import typing

def get_tickers(filepath: str) -> typing.List[str]:
    """ returns list of tickers from csv file """
    df = pd.read_csv(filepath)
    tickers = df['ticker']
    return tickers
