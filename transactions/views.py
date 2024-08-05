from django.shortcuts import render, redirect 
from django.urls import reverse 
from .models import * 


def index(request):
    coins = CryptoCoin.objects.all()
    context = {}
    for coin in coins:
        context[coin.symbol] = CryptoPrice.objects.filter(coin=coin).order_by('-timestamp').first()
    # print(context)
    return render(request, 'index.html', context)


def create_buy_view(request):
    if request.method == 'POST':
        amount = request.POST.get('buy-amount')
        coin_name = request.POST.get('buy-option')
        price_transfer = request.POST.get('buy-transfer')
        buy_currency = request.POST.get('buy-currency')
        user_email = request.POST.get('email')
        wallet_address = request.POST.get('wallet-address')

        coin = CryptoCoin.objects.get(symbol=coin_name)
        # print(coin_name)

        buy_transaction = BuyTransaction.objects.create(
            amount=float(amount),
            coin_name=coin_name,
            coin=coin,
            price_transfer=float(price_transfer),
            user_email=user_email,
            wallet_address=wallet_address,
            fee=float(amount)*0.000005,
            remain=float(amount)*0.999995,
        )

        return redirect(reverse('buy-detail', kwargs={'guid': buy_transaction.guid}))


    buyAmount = request.GET.get('buy-amount')
    buyOption = request.GET.get('buy-option')
    buyTransfer = request.GET.get('buy-transfer')
    buyCurrency = request.GET.get('buy-currency')

    print(buyAmount)
    print(buyOption)
    print(buyTransfer)
    print(buyCurrency)
    context = {}
    context['buyAmount'] = buyAmount
    context['buyOption'] = buyOption
    context['buyTransfer'] = buyTransfer    
    context['buyCurrency'] = buyCurrency
    context['fee'] = float(buyAmount) * 0.000005
    context['remain'] = float(buyAmount) * 0.999995

    return render(request, 'create-buy.html', context)


def buy_detail_view(request, guid):
    try:
        buy_trans = BuyTransaction.objects.get(guid=guid)
    except BuyTransaction.DoesNotExits():
        return redirect('index')
    context  = {}
    context['buy_trans'] = buy_trans
    return render(request, 'buy-detail.html', context)


def create_sell_view(request):
    return render(request, 'create-sell.html')
