from django.conf import settings
from enum import Enum

class CurrencyLayerCommand(Enum):
    LIST_CURRENCIES = 'list'

class EndpointsFactory:

    @staticmethod
    def command(commandEnum):
        return f'{settings.CURRENCY_LAYER_API}/{commandEnum.value}?access_key={settings.CURRENCY_LAYER_KEY}'
