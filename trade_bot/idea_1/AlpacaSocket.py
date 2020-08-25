from decouple import config
import alpaca_trade_api as alpaca


class AlpacaPaperSocket(alpaca.REST):
    def __init__(self):
        super().__init__(
            key_id=config('ALPACA_PAPER_KEY_ID'),
            secret_key=config('ALPACA_PAPER_SECRET_KEY'),
            base_url='https://paper-api.alpaca.markets',
            api_version='v2'
        )
