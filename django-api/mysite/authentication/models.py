# djsr/authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    source = models.CharField(max_length=50, default='both')
    currency = models.CharField(max_length=50, null=True)

class Advice(models.Model):
    id = models.AutoField(primary_key=True)
    currency = models.CharField(max_length=32)
    operation_type = models.CharField(max_length=32)
    entry = models.CharField(max_length=32)
    
    datetime = models.DateField()
    source = models.CharField(max_length=32)

    class Meta:
        db_table = "advice"

class TakeProfit(models.Model):
    id = models.AutoField(primary_key=True)
    entry = models.CharField(max_length=32)
    advice = models.ForeignKey(Advice, related_name='take_profits', on_delete=models.CASCADE)

    class Meta:
        db_table = "takeProfit"

class StopLoss(models.Model):
    id = models.AutoField(primary_key=True)
    entry = models.CharField(max_length=32)
    advice = models.ForeignKey(Advice, related_name='stop_losses', on_delete=models.CASCADE)

    class Meta:
        db_table = "stoploss"

# Advice.take_profits = models.ForeignKey(TakeProfit, null=True, on_delete=models.CASCADE)
# Advice.stop_losses = models.ForeignKey(StopLoss, null=True, on_delete=models.CASCADE)

# class Note(models.Model):
    # id = models.AutoField(primary_key=True)
    # title = models.CharField(verbose_name='Заголовок', max_length=32, blank=True)
    # text = models.TextField(verbose_name='Текст', blank=True)
    # isPinned = models.BooleanField(verbose_name='Закреплено', default=False )
    # author = models.ForeignKey(
    #     CustomUser,
    #     on_delete=models.CASCADE,
    #     null=True
    # )
    # def __str__(self):
    #     return self.title 