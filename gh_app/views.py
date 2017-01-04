# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from .models import Post, AirWater_Filter, AirWater_EquipmentConsumable, Career

# Create your views here.

def New(request):
	firstfour = Post.objects.order_by("-upload_date")[:4]
	post1 = firstfour[0]
	post2 = firstfour[1]
	post3 = firstfour[2]
	post4 = firstfour[3]
	rest = Post.objects.order_by("-upload_date")[4:]
	return render(request, 'new.html', {"post1" : post1,"post2" : post2,"post3" : post3,"post4" : post4})

def Archive(request):
	posts = Post.objects.order_by("-upload_date")
	return render(request, 'archive.html', {"posts" : posts})

def AboutUs(request):
	context = {}
	return render(request, 'about_us.html', context)

def Products(request):
	filters = AirWater_Filter.objects.all()
	equipment_consumables = AirWater_EquipmentConsumable.objects.all()
	return render(request, 'products.html', {"filters" : filters, "equipment_consumables" : equipment_consumables})

def Careers(request):
	careers = Career.objects.order_by("title")
	return render(request, 'careers.html', {"careers" : careers})

def ContactUs(request):
	context = {}
	return render(request, 'contact_us.html', context)


