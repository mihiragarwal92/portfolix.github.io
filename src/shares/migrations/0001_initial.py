# Generated by Django 4.1 on 2022-08-28 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(choices=[('NASDAQ', 'NASDAQ'), ('NYSE', 'NYSE'), ('BSE', 'BSE'), ('NSE', 'NSE'), ('NSE/BSE', 'NSE/BSE')], max_length=10)),
                ('symbol', models.CharField(max_length=20)),
                ('user', models.IntegerField()),
                ('goal', models.IntegerField(blank=True, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('conversion_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Conversion Price')),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Buy Price')),
                ('buy_value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Buy Value')),
                ('latest_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Price')),
                ('latest_value', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Value')),
                ('as_on_date', models.DateField(blank=True, null=True, verbose_name='As On Date')),
                ('gain', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Gain')),
                ('notes', models.CharField(blank=True, max_length=80, null=True)),
                ('realised_gain', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Realised Gain')),
                ('etf', models.BooleanField(default=False)),
                ('roi', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
            options={
                'unique_together': {('exchange', 'symbol', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_date', models.DateField(verbose_name='Transaction Date')),
                ('trans_type', models.CharField(choices=[('Buy', 'Buy'), ('Sell', 'Sell')], max_length=10)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Price')),
                ('quantity', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('conversion_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Conversion Rate')),
                ('trans_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Total Price')),
                ('broker', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.CharField(blank=True, max_length=80, null=True)),
                ('div_reinv', models.BooleanField(default=False)),
                ('share', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shares.share')),
            ],
            options={
                'unique_together': {('share', 'trans_date', 'price', 'quantity', 'trans_type', 'broker')},
            },
        ),
    ]
