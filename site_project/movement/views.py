from django.shortcuts import render
from django.http import HttpResponse

from .models import Activity, Fitbit

# Create your views here.
def index(request):
	return HttpResponse("Movement test")
