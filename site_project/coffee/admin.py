from django.contrib import admin

from .models import Coffee


class CoffeeAdmin(admin.ModelAdmin):
	list_display = ( 'consumption_date', 'coffee_count', 'location')

# Register your models here.
admin.site.register(Coffee)
