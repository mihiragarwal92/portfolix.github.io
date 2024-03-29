# Generated by Django 4.1 on 2022-08-28 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSUAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(choices=[('NASDAQ', 'NASDAQ'), ('NYSE', 'NYSE'), ('BSE', 'BSE'), ('NSE', 'NSE')], max_length=10)),
                ('symbol', models.CharField(max_length=20)),
                ('user', models.IntegerField()),
                ('goal', models.IntegerField(blank=True, null=True)),
                ('award_date', models.DateField(verbose_name='Award Date')),
                ('award_id', models.CharField(max_length=20)),
                ('shares_awarded', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Awarded')),
            ],
        ),
        migrations.CreateModel(
            name='RestrictedStockUnits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vest_date', models.DateField(verbose_name='Vest Date')),
                ('fmv', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='FMV')),
                ('aquisition_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Aquisition Price')),
                ('shares_vested', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Vested')),
                ('shares_for_sale', models.DecimalField(decimal_places=0, max_digits=20, verbose_name='Available For Sell At Vest')),
                ('conversion_rate', models.DecimalField(decimal_places=2, default=1, max_digits=20, verbose_name='Conversion Price')),
                ('total_aquisition_price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Total Aquisition Price')),
                ('notes', models.CharField(blank=True, max_length=80, null=True)),
                ('unsold_shares', models.DecimalField(decimal_places=0, default=0, max_digits=20, verbose_name='Unsold Quantity')),
                ('latest_conversion_rate', models.DecimalField(decimal_places=2, default=1, max_digits=20, verbose_name='Latest Conversion Price')),
                ('latest_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Latest Price')),
                ('latest_value', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Latest Value')),
                ('as_on_date', models.DateField(blank=True, null=True, verbose_name='As On Date')),
                ('realised_gain', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Realised Gain')),
                ('unrealised_gain', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Unrealised Gain')),
                ('tax_at_vest', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Tax at Vest')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rsu.rsuaward')),
            ],
            options={
                'unique_together': {('award', 'vest_date')},
            },
        ),
        migrations.CreateModel(
            name='RSUSellTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_date', models.DateField(verbose_name='Transaction Date')),
                ('price', models.DecimalField(decimal_places=4, max_digits=20, verbose_name='Price')),
                ('units', models.DecimalField(decimal_places=4, max_digits=20)),
                ('conversion_rate', models.DecimalField(decimal_places=2, default=1, max_digits=20, verbose_name='Conversion Rate')),
                ('trans_price', models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='Total Price')),
                ('realised_gain', models.DecimalField(decimal_places=2, default=0, max_digits=20, verbose_name='Realised Gain')),
                ('notes', models.CharField(blank=True, max_length=80, null=True)),
                ('rsu_vest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rsu.restrictedstockunits')),
            ],
            options={
                'unique_together': {('rsu_vest', 'trans_date')},
            },
        ),
    ]
