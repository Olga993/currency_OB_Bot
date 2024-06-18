import requests
import json
from config import keys


class ApiException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):
        if quote == base:
            raise ApiException(f'Невозможно перевести одинаковые валюты {base}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ApiException(f'Введено неверное значение валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ApiException(f'Введено неверное значение валюты {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ApiException(f'Неправильно введено число {amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        total_quote = json.loads(r.content)[keys[quote]] * amount
        return total_quote


