from django.core.management.base import BaseCommand
from currency_layer_api.apps import CurrencyLayerApi
from currency_layer_api.models import Currency
from django.db.models.base import ModelState
from telegram_bot.models import Subscription

###
### Watch subscription and send reminder
###

class Command(BaseCommand):
    help = 'Watch subscription and send reminder'

    def handle(self, *args, **argv):
        api = CurrencyLayerApi()

        subs = Subscription.objects.all()
        ## Array containing all the rates to fetch
        currencies_list = list(map(lambda x: (x['currency_from_id'], x['currency_to_id']), subs.values()))

        # Clean duplicates and fetch rates
        try:
            rates = api.get_rates(list(dict.fromkeys(currencies_list)))
        except:
            raise Exception("Could not fetch rates")
        # {from_currency_id, to_currency_id, rate}
        for rate in rates:
            for sub in subs.filter(
                currency_from_id=rate['from_currency_id'],
                currency_to_id=rate['to_currency_id'],
                max_rate__gt=rate['rate']
            ).all():
                self.send_reminder(sub)


    def println(self, str):
        self.stdout.write(str, ending='\n')

    def send_reminder(self, sub):
        self.println(f'Send reminder to {sub.chat_id}')
