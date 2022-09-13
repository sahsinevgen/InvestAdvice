# Generated by Django 4.1.1 on 2022-09-15 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_stoploss_advice_alter_takeprofit_advice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stoploss',
            name='advice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.advice', verbose_name='advice_id'),
        ),
        migrations.AlterField(
            model_name='takeprofit',
            name='advice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.advice', verbose_name='advice_id'),
        ),
    ]
