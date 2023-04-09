# Generated by Django 4.1 on 2022-08-28 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=20, unique=True)),
                ('collection_start_date', models.DateField(verbose_name='Collection Start Date')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MFCategoryReturns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, unique=True)),
                ('return_1d_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1D Avg')),
                ('return_1w_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1W Avg')),
                ('return_1m_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1M Avg')),
                ('return_3m_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3M Avg')),
                ('return_6m_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='6M Avg')),
                ('return_1y_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1Y Avg')),
                ('return_3y_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3Y Avg')),
                ('return_5y_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='5Y Avg')),
                ('return_10y_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='10Y Avg')),
                ('return_15y_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='15Y Avg')),
                ('return_inception_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Inception Avg')),
                ('return_ytd_avg', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='YTD Avg')),
                ('return_1d_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1D Top')),
                ('return_1w_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1W Top')),
                ('return_1m_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1M Top')),
                ('return_3m_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3M Top')),
                ('return_6m_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='6M Top')),
                ('return_1y_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1Y Top')),
                ('return_3y_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3Y Top')),
                ('return_5y_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='5Y Top')),
                ('return_10y_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='10Y Top')),
                ('return_15y_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='15Y Top')),
                ('return_inception_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Inception Top')),
                ('return_ytd_top', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='YTD Top')),
                ('return_1d_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1D Bottom')),
                ('return_1w_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1W Bottom')),
                ('return_1m_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1M Bottom')),
                ('return_3m_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3M Bottom')),
                ('return_6m_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='6M Bottom')),
                ('return_1y_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1Y Bottom')),
                ('return_3y_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3Y Bottom')),
                ('return_5y_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='5Y Bottom')),
                ('return_10y_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='10Y Bottom')),
                ('return_15y_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='15Y Bottom')),
                ('return_inception_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Inception Bottom')),
                ('return_ytd_bot', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='YTD Bottom')),
                ('as_on_date', models.DateField(blank=True, null=True, verbose_name='As On Date')),
            ],
        ),
        migrations.CreateModel(
            name='MutualFund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=200)),
                ('isin', models.CharField(max_length=20)),
                ('isin2', models.CharField(blank=True, max_length=20, null=True)),
                ('fund_house', models.CharField(blank=True, max_length=50, null=True)),
                ('kuvera_name', models.CharField(blank=True, max_length=200, null=True)),
                ('collection_start_date', models.DateField(verbose_name='Collection Start Date')),
                ('bse_star_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ms_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ms_id', models.CharField(blank=True, max_length=20, null=True)),
                ('return_1d', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1D')),
                ('return_1w', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1W')),
                ('return_1m', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1M')),
                ('return_3m', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3M')),
                ('return_6m', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='6M')),
                ('return_1y', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='1Y')),
                ('return_3y', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='3Y')),
                ('return_5y', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='5Y')),
                ('return_10y', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='10Y')),
                ('return_15y', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='15Y')),
                ('return_incep', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Inception')),
                ('return_ytd', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='YTD')),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('investment_style', models.CharField(blank=True, max_length=200, null=True)),
                ('as_on_date', models.DateField(blank=True, null=True, verbose_name='As On Date')),
            ],
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timezone', models.CharField(default='Asia/Kolkata', max_length=100)),
                ('indexes_to_scroll', models.CharField(blank=True, max_length=20000, null=True)),
                ('document_backup_locn', models.CharField(blank=True, max_length=20000, null=True)),
                ('currency', models.CharField(blank=True, default='INR', max_length=3, null=True)),
                ('show_zero_value_mfs', models.BooleanField(default=False)),
                ('show_zero_value_shares', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScrollData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrip', models.CharField(max_length=100, unique=True)),
                ('val', models.DecimalField(decimal_places=2, max_digits=20)),
                ('change', models.DecimalField(decimal_places=2, max_digits=20)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateTimeField()),
                ('display', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.CharField(choices=[('NASDAQ', 'NASDAQ'), ('NYSE', 'NYSE'), ('BSE', 'BSE'), ('NSE', 'NSE'), ('NSE/BSE', 'NSE/BSE')], max_length=10)),
                ('symbol', models.CharField(max_length=20)),
                ('isin', models.CharField(default='', max_length=20)),
                ('collection_start_date', models.DateField(verbose_name='Collection Start Date')),
                ('capitalisation', models.CharField(blank=True, choices=[('Large-Cap', 'Large-Cap'), ('Mid-Cap', 'Mid-Cap'), ('Small-Cap', 'Small-Cap'), ('Micro-Cap', 'Micro-Cap')], max_length=15, null=True)),
                ('industry', models.CharField(blank=True, max_length=50, null=True)),
                ('etf', models.BooleanField(default=False)),
                ('trading_status', models.CharField(choices=[('Listed', 'Listed'), ('Delisted', 'Delisted')], default='Listed', max_length=25)),
                ('delisting_date', models.DateField(blank=True, null=True, verbose_name='Delisting Date')),
                ('listing_date', models.DateField(blank=True, null=True, verbose_name='Listing Date')),
                ('suspension_date', models.DateField(blank=True, null=True, verbose_name='Suspension Date')),
            ],
            options={
                'unique_together': {('exchange', 'symbol')},
            },
        ),
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('user_id', models.CharField(max_length=50)),
                ('password', models.BinaryField()),
                ('additional_password', models.BinaryField(null=True)),
                ('additional_input', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=50)),
                ('last_updated', models.DateField()),
                ('notes', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'unique_together': {('user', 'user_id', 'source')},
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('yahoo_symbol', models.CharField(max_length=20)),
            ],
            options={
                'unique_together': {('country', 'name')},
            },
        ),
        migrations.CreateModel(
            name='HistoricalGoldPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price')),
                ('buy_type', models.CharField(choices=[('Physical', 'Physical'), ('Digital', 'Digital')], max_length=10)),
                ('purity', models.CharField(choices=[('22K', '22K'), ('24K', '24K')], max_length=10)),
            ],
            options={
                'unique_together': {('buy_type', 'purity', 'date')},
            },
        ),
        migrations.CreateModel(
            name='HistoricalForexRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_cur', models.CharField(max_length=20, verbose_name='From Currency')),
                ('to_cur', models.CharField(max_length=20, verbose_name='To Currency')),
                ('date', models.DateField(verbose_name='Date')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Conversion Rate')),
            ],
            options={
                'unique_together': {('from_cur', 'to_cur', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Splitv2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_fv', models.DecimalField(decimal_places=2, max_digits=20)),
                ('new_fv', models.DecimalField(decimal_places=2, max_digits=20)),
                ('announcement_date', models.DateField()),
                ('ex_date', models.DateField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.stock')),
            ],
            options={
                'unique_together': {('stock', 'announcement_date')},
            },
        ),
        migrations.CreateModel(
            name='MFYearlyReturns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('returns', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('diff_index', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('diff_category', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('percentile_rank', models.IntegerField(blank=True, null=True)),
                ('funds_in_category', models.IntegerField(blank=True, null=True)),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.mutualfund')),
            ],
            options={
                'unique_together': {('fund', 'year')},
            },
        ),
        migrations.CreateModel(
            name='HistoricalStockPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Price')),
                ('symbol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.stock')),
            ],
            options={
                'unique_together': {('symbol', 'date')},
            },
        ),
        migrations.CreateModel(
            name='HistoricalMFPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('nav', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='NAV')),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.mutualfund')),
            ],
            options={
                'unique_together': {('code', 'date')},
            },
        ),
        migrations.CreateModel(
            name='HistoricalIndexPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('points', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Points')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.index')),
            ],
            options={
                'unique_together': {('index', 'date')},
            },
        ),
        migrations.CreateModel(
            name='HistoricalCoinPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('price', models.DecimalField(decimal_places=10, max_digits=30, verbose_name='Price')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.coin')),
            ],
            options={
                'unique_together': {('coin', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Dividendv2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('announcement_date', models.DateField()),
                ('ex_date', models.DateField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.stock')),
            ],
            options={
                'unique_together': {('stock', 'announcement_date')},
            },
        ),
        migrations.CreateModel(
            name='Bonusv2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio_num', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ratio_denom', models.DecimalField(decimal_places=2, max_digits=20)),
                ('announcement_date', models.DateField()),
                ('record_date', models.DateField()),
                ('ex_date', models.DateField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.stock')),
            ],
            options={
                'unique_together': {('stock', 'announcement_date')},
            },
        ),
    ]
