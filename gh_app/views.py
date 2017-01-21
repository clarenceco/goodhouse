# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError


from .models import Post, AirWater_Filter, AirWater_EquipmentConsumable, Career, ContactForm, SearchBox

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

def OpenTab(request, filter_name):
	filters = AirWater_Filter.objects.all()
	equipment_consumables = AirWater_EquipmentConsumable.objects.all()
	objlist = []
	for x in filters:
		if str(x.name) == str(filter_name):
			objlist.append(x)
			return render(request,'prod.html',{'objlist': objlist})
	for y in equipment_consumables:
		if str(y.name) == str(filter_name):
			objlist.append(y)
			return render(request,'prod.html',{'objlist': objlist})
	return render(request,'prod.html',{'objlist': objlist})

def Search(request):
	filters = AirWater_Filter.objects.all()
	equipment_consumables = AirWater_EquipmentConsumable.objects.all()
	if request.method == 'POST':
		search = SearchBox(request.POST)
		if search.is_valid():
			objlist = []
			search_string = search.cleaned_data['search']
			for x in filters:
				if str(search_string) in str(x.name):
					objlist.append(x)
			for y in equipment_consumables:
				if str(search_string) in str(y.name):
					objlist.append(y)
			return render(request, 'search.html', {'objlist' : objlist, 'len' : len(objlist)})
		else:
			return render(request, 'products.html', {"filters" : filters, "equipment_consumables" : equipment_consumables})

	return render(request, 'products.html', {"filters" : filters, "equipment_consumables" : equipment_consumables})
	
def Careers(request):
	careers = Career.objects.order_by("title")
	return render(request, 'careers.html', {"careers" : careers})

def ContactUs(request):
	context = {}
	return render(request, 'contact_us.html', context)


def Send(request):
	context = {}
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			number = form.cleaned_data['number']
			content = form.cleaned_data['content']
			fullemail = "Name: " + name + "\nEmail:" + email + "\nNumber: " + number + "\n\nContent: " + content
			try:
				send_mail("Website Message", fullemail, settings.EMAIL_HOST_USER, ['goodhousetestacc@gmail.com'], fail_silently=False)
				return render(request, 'contact_us.html', context)
			except:
				return render(request, 'contact_us.html', context)
		else:
			return render(request, 'contact_us.html', context)
	else:
		return render(request, 'contact_us.html', context)

