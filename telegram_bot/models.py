from django.db import models
from djmoney.models.fields import MoneyField
from uuid import uuid4
from currency_layer_api.models import Currency

# Create your models here.
class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    chat_id = models.TextField(max_length=55)
    currency_from = models.ForeignKey(
        Currency,
        related_name="from_subscriptions",
        on_delete=models.PROTECT,
        blank=False,
        null=True
    )
    currency_to = models.ForeignKey(
        Currency,
        related_name="to_subscriptions",
        on_delete=models.PROTECT,
        blank=False,
        null=True
    )
    max_rate = MoneyField(max_digits=14, decimal_places=2)

    @classmethod
    def new(cls, chat_id, from_currency, to_currency, rate):
        inst = cls()
        inst.chat_id = chat_id
        inst.currency_from = from_currency
        inst.currency_to = to_currency
        inst.max_rate = rate
        return inst