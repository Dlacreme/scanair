from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from telegram_bot.models import Subscription
from .services import subscribe

### PAYLOAD EXAMPLE
### {
###  "from": "EUR",
###  "to": "USD",
###  "rate": 1.05
### }
###

@api_view(['POST'])
def webhook(req):
    fr = req.data['from']
    to = req.data['to']
    rate = req.data['rate']
    if type(fr) is not str or type(to) is not str or (type(rate) is not int and type(rate) is not float):
        return Response(status = 400, data = {'ok': False, 'description': 'Invalid payload'})
    try:
        subscribe('defaulttest', fr, to, rate)
    except Exception as err:
        return Response(status = 400, data = {'ok': False, 'description': f'{err}'})
    return Response({'ok': True, 'description': f'You will be notified when {fr} to {to} is below {rate}'})
