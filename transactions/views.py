from django.shortcuts import render
from .models import * 


def index(request):
    coins = CryptoCoin.objects.all()
    context = {}
    for coin in coins:
        context[coin.symbol] = CryptoPrice.objects.filter(coin=coin).order_by('-timestamp').first()
    # print(context)
    return render(request, 'index.html', context)
