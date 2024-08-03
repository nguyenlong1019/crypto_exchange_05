from django.db import models
from django.utils import timezone 


class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('buy', 'buy'),
        ('sell', 'sell'),
    )

    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
        verbose_name='id', help_text='Khóa chính mỗi transaction')
    tx_hash = models.CharField(max_length=66, unique=True)
    sender = models.CharField(max_length=42)
    receiver = models.CharField(max_length=42)
    transaction_type = models.CharField(max_length=15, default='buy', choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Giao dịch'
        verbose_name_plural = 'Giao dịch'
        db_table = 'transactions'
    
    def __str__(self):
        return f"{self.id} - {self.tx_hash}"


class CryptoCoin(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False,
        verbose_name='id')
    name = models.CharField(max_length=255, null=True, blank=True)
    symbol = models.CharField(max_length=7)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('symbol',)
        verbose_name = 'Tiền điện tử'
        verbose_name_plural = 'Tiền điện tử'
        db_table = 'crypto_coin'

    def __str__(self):
        return f"{self.symbol} - {self.name if self.name else ''}"
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        super(CryptoCoin, self).save(*args, **kwargs)


class CryptoPrice(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False,
        verbose_name='id', help_text='Khóa chính bảng giá tiền điện tử')
    coin = models.ForeignKey(CryptoCoin, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)
        verbose_name = 'Giá tiền điện tử'
        verbose_name_plural = 'Giá tiền điện tử'
        db_table = 'crypto_price'
    
    def __str__(self):
        return f"{self.coin.symbol if self.coin else self.id} - {self.price}"
    
