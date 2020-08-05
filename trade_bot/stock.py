""" webscape stock data """


import time

import requests
from bs4 import BeautifulSoup
from constants import MIN_FRACTION_BLOWING


class Stock:
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker.upper()

        self.__time = time.time()

        self.price = None
        self.open_price = None
        self.volume = None
        self.avg_volume = None
        self.change = None
        self.volume_dif_fraction = None
        self.overnight_change = None
        self.day_change = None
        self.load_data()

    def load_data(self) -> None:
        """ webscape stock data """
        yahoo_result = requests.get("https://finance.yahoo.com/quote/" + self.ticker)
        robin_result = requests.get('https://robinhood.com/stocks/' + self.ticker)

        yahoo_soup = BeautifulSoup(yahoo_result.content, features="html.parser")
        robin_soup = BeautifulSoup(robin_result.content, features="html.parser")

        # this section will error if Robin Hood or Yahoo don't have info on the specified stock
        self.price = float(robin_soup.find_all(
            attrs={"class": "QzVHcLdwl2CEuEMpTUFaj"})[0].text.replace(',', '')[1:])

        try:
            ocs = robin_soup.find_all(
                attrs={"class": "_3Flirkl1fA47PUu1VVzeHZ"})[0].text
            self.overnight_change = float(ocs[ocs.index('(') + 1:ocs.index(')') - 1])
        except Exception as e:
            print(f'unable to fetch overnight change for ${self.ticker}')

        try:
            dcs = robin_soup.find_all(
                attrs={"class": "_27rSsse3BjeLj7Y1bhIE_9"})[0].text
            self.day_change = float(dcs[dcs.index('(') + 1:dcs.index(')') - 1])
        except Exception as e:
            print(f'unable to fetch daily change for ${self.ticker}')

        self.open_price = float(yahoo_soup.find_all(
            attrs={"data-test": "OPEN-value"})[0].text.replace(',', ''))

        self.volume = int(yahoo_soup.find_all(
            attrs={"data-test": "TD_VOLUME-value"})[0].text.replace(',', ''))

        self.avg_volume = int(yahoo_soup.find_all(
            attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"})[0].text.replace(',', ''))

        self.change = (self.price - self.open_price) * 100/self.open_price
        self.volume_dif_fraction = (self.volume - self.avg_volume) / self.avg_volume

    def is_blowing(self) -> bool:  # DELETE ME
        """ If the current volume is above the average volume by enough then the stock is considered 'blowing' """
        return self.volume_dif_fraction > MIN_FRACTION_BLOWING

    def __print_time_dif(self, title: str = '') -> None:  # for testing
        print(title, 'time (s):', time.time() - self.__time)
        self.__time = time.time()

    def __str__(self) -> str:
        return '\n' + '\n\t'.join(f'{key}: {value}' for key, value in vars(self).items() if not key.startswith('_')) + '\n'


if __name__ == '__main__':
    kodk = Stock('kodk')
    print(kodk)
