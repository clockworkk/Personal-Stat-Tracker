from django.contrib import admin

from .models import Activity, Fitbit

class ActivityAdmin(admin.ModelAdmin):
	fieldsets = [
		('Date Information', {'fields': ['entry_date']}),
		('Fitbit Data', {'fields': ['steps', 'distance'], 'classes' : ['collapse']}),
	]
	list_display = ('entry_date' , 'steps', 'distance')

class FitbitAdmin(admin.ModelAdmin):
	fieldsets = [
		('Date Information', {'fields': ['entry_date']}),
		('Fitbit Data', {'fields': ['steps', 'distance', 'active_minutes', 'weight'], 'classes' : ['collapse']}),
	]
	list_display = ('entry_date', 'steps', 'distance', 'active_minutes', 'weight')

# Register your models here.
admin.site.register(Activity)
admin.site.register(Fitbit)
