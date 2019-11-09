from .models import Currency

def get_currencies_or_fail(from_currency_id, to_currency_id):
    currencies = Currency.objects.filter(pk__in=[from_currency_id, to_currency_id])
    return (get_currency_or_fail(currencies, from_currency_id), get_currency_or_fail(currencies, to_currency_id))

def get_currency_or_fail(query_set, currency_id):
    try:
        return query_set.filter(id=currency_id).get()
    except:
        raise Exception(f'{currency_id} is not existing')
