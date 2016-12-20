# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Post, AirWater_Filter, AirWater_EquipmentConsumable


# Create your views here.

def HomePage(request):
	context = {}
	return render(request, 'base.html', context)

def AboutUs(request):
	context = {}
	return render(request, 'about_us.html', context)

def Careers(request):
	context = {}
	return render(request, 'careers.html', context)

def ContactUs(request):
	context = {}
	return render(request, 'contact_us.html', context)

def Products(request):
	context = {}
	return render(request, 'products.html', context)


