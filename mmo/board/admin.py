from django.contrib import admin

from django.contrib import admin
from .models import Ads


class AdsAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'player', 'dateCreation']
    list_filter = ('player', 'dateCreation')


admin.site.register(Ads, AdsAdmin)
