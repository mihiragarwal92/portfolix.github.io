from django.contrib import admin
from solo.admin import SingletonModelAdmin

#from .models import Stock, HistoricalStockPrice, MutualFund, HistoricalMFPrice, HistoricalForexRates, MFYearlyReturns, MFCategoryReturns, ScrollData, Preferences, Index, HistoricalIndexPoints
from .models import *

admin.site.register(Stock)
admin.site.register(HistoricalStockPrice)
admin.site.register(MutualFund)
admin.site.register(HistoricalMFPrice)
admin.site.register(HistoricalForexRates)
admin.site.register(MFYearlyReturns)
admin.site.register(MFCategoryReturns)
admin.site.register(ScrollData)
admin.site.register(Preferences, SingletonModelAdmin)
admin.site.register(Dividendv2)
admin.site.register(Bonusv2)
admin.site.register(Splitv2)
admin.site.register(HistoricalGoldPrice)
admin.site.register(Index)
admin.site.register(HistoricalIndexPoints)
admin.site.register(Coin)
admin.site.register(HistoricalCoinPrice)