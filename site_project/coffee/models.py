from django.db import models

# Create your models here.
class Coffee(models.Model):
	coffee_count = models.IntegerField(default=0)
	consumption_date = models.DateTimeField('date consumed')
	location = models.CharField(max_length=50)
