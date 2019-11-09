from currency_layer_api.view_models.base import BaseViewModel
from currency_layer_api.models import Currency

class CurrencyList(BaseViewModel):

    # self.currencies = Currency[]

    def __init__(self, http_response_data):
        super().__init__(http_response_data)
        self.currencies = CurrencyList.raw_currency_list(http_response_data['currencies'])

    @staticmethod
    def raw_currency_list(list):
        res = []
        for key, value in list.items():
            res.append(Currency(key, value))
        return res
