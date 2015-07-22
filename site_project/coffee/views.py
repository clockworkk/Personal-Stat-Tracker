from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Coffee

# Create your views here.
def index(request):
	return HttpResponse("Coffee test")
