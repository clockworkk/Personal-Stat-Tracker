import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Activity(models.Model):
	entry_date = models.DateTimeField('date of entry')
	steps = models.IntegerField(default=0)
	distance = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)

	def __str__(self):
		return "Date: " + str(self.entry_date) + ", Steps: " + str(self.steps) + ", Distance: " + str(self.distance)

class Fitbit(models.Model):
	entry_date = models.DateTimeField('date of entry')
	steps = models.IntegerField(default=0)
	distance = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
	weight = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
	active_minutes = models.IntegerField(default=0)

	def __str__(self):
		return "Date: " + str(self.entry_date) + ", Steps: " + str(self.steps) + ", Distance: " + str(self.distance)
