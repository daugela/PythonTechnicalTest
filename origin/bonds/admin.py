from django.contrib import admin

from .models import Bonds


@admin.register(Bonds)
class BondsAdmin(admin.ModelAdmin):
    pass

