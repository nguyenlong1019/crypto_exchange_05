from django.contrib import admin
from .models import * 


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ['tx_hash', 'sender', 'receiver']


@admin.register(CryptoCoin)
class CryptoCoinAdmin(admin.ModelAdmin):
    search_fields = ['name', 'symbol']


@admin.register(CryptoPrice)
class CryptoPriceAdmin(admin.ModelAdmin):
    search_fields = ['coin', 'price']

