from django.core.management.base import BaseCommand
from currency_layer_api.apps import CurrencyLayerApi
from currency_layer_api.models import Currency
from django.db.models.base import ModelState

###
### Import all currencies supported by Currency Layer API into our Database.
###

class Command(BaseCommand):
    help = 'Import all currencies supported by Currency Layer Api'

    def handle(self, *args, **argv):
        api = CurrencyLayerApi()
        currencies_wrapper = api.currency_list()
        if currencies_wrapper.is_failure():
            raise Exception('Could not fetch available currencies')
        print(f'Fetched: [{currencies_wrapper.method}] {currencies_wrapper.url}')
        state = ModelState()
        state.adding = True
        for cur in currencies_wrapper.result.currencies:
            cur._state = state
        Currency.objects.bulk_create(currencies_wrapper.result.currencies)

    def println(self, str):
        self.stdout.write(str, ending='\n')
