from django.conf import settings 
import json 
import random 
import requests 
from transactions.models import * 
from datetime import datetime 


def get_crypto_prices():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin,ethereum,tether',
        'vs_currencies': 'vnd'
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data 


def get_bnb_price():
    url = 'https://api.binance.com/api/v3/ticker/price'
    symbol = 'BNBUSDT'
    response = requests.get(url, params={'symbol': symbol})
    data = response.json()
    if 'price' in data:
        return float(data['price'])
    else:
        return None 


def update_coin_price_vnd():
    coins = CryptoCoin.objects.all()
    crypto_prices = get_crypto_prices()
    btc = crypto_prices['bitcoin']['vnd']
    eth = crypto_prices['ethereum']['vnd']
    usdt = crypto_prices['tether']['vnd']
    bnb = get_bnb_price() * float(usdt)

    for coin in coins:
        if coin.symbol == 'BTC':
            try:
                btc_price = CryptoPrice.objects.create(
                    coin=coin,
                    price=float(btc)
                )
            except:
                pass 
        elif coin.symbol == 'ETH':
            try:
                eth_price = CryptoPrice.objects.create(
                    coin=coin,
                    price=float(eth)
                )
            except:
                pass 
        elif coin.symbol == 'USDT':
            try:
                usdt_price = CryptoPrice.objects.create(
                    coin=coin,
                    price=float(usdt)
                )
            except:
                pass 
        elif coin.symbol == 'BNB':
            try:
                bnb_price = CryptoPrice.objects.create(
                    coin=coin,
                    price=float(bnb)
                )
            except:
                pass 
        else:
            pass 

    print(f"btc: {btc} saved!")
    print(f"eth: {eth} saved!")
    print(f"usdt: {usdt} saved!")
    print(f"bnb: {bnb} saved!")



