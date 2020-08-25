import threading
import requests, json
from constants import *


def get_account_info():
    print('getting account info')

    r = requests.get(ACC_URL, headers=HEADERS)
    return json.loads(r.content)


def create_order(ticker, qty, side, order_type, time_in_force):
    print('creating order')

    data = {
        'symbol': ticker,
        'qty': qty,
        'side': side,
        'type': order_type,
        'time_in_force': time_in_force
    }

    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)


def get_market_data(tickers):
    # this does not work yet plz figure out <3
    data = {
        'symbols': ','.join(tickers)
    }
    r = requests.get(BAR_URL, json=data, headers=HEADERS)
    return json.loads(r.content)


if __name__ == '__main__':
    #print(get_market_data(['AAPL']))
    print(get_account_info())
