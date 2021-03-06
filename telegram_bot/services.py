from currency_layer_api.services import get_currencies_or_fail
from .models import Subscription

def subscribe(chat_id, from_currency_id, to_currency_id, rate):
    # Get currencies
    (from_currency, to_currency) = get_currencies_or_fail(from_currency_id, to_currency_id)
    # Remove existing subscription using the same currencies
    disable_existing_subscription(from_currency_id, to_currency_id)
    # Create new Subscription
    Subscription.new(chat_id, from_currency, to_currency, rate).save()

def disable_existing_subscription(from_currency_id, to_currency_id):
    try:
        Subscription.objects.filter(currency_from_id=from_currency_id, currency_to_id=to_currency_id).delete()
    except:
        # Entry not existing - all good
        return
