import requests
import json
from django.apps import AppConfig
from django.conf import settings

from currency_layer_api.endpoints import EndpointsFactory, CurrencyLayerCommand
from currency_layer_api.response_wrapper import ResponseWrapper
from currency_layer_api.view_models.currency_list import CurrencyList


class CurrencyLayerApiConfig(AppConfig):
    name = 'currency_layer_api'


class CurrencyLayerApi():

    def __init__(self):
        return

    def currency_list(self):
        url = EndpointsFactory.command(CurrencyLayerCommand.LIST_CURRENCIES)
        res = requests.get(url)
        return ResponseWrapper(res.status_code, url, 'GET', None, CurrencyList(res.json()))

    # Currencies (CURRENCY_FROM, CURRENCY_TO)
    def get_rates(self, currencies):
        url = EndpointsFactory.command(CurrencyLayerCommand.CHANGE)
        rates = []
        ## the Api does not allow us to fetch many rates at the same time
        for pair in currencies:
            res = requests.get(f'{url}&currencies={pair[0]},{pair[1]}').json()
            rates.append({'from_currency_id': pair[0], 'to_currency_id': pair[1], 'rate': res['rate']})
        return rates
