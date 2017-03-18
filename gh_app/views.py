# -*- coding: utf-8 -*-
from __future__ import unicode_literals 
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError


from .models import Post, Air_Filter, Water_Filter, Dust_Filter, Featured_Product, Career, ContactForm, SearchBox, Service

# Create your views here.

def New(request):
	firstfour = Post.objects.order_by("-upload_date")[:4]
	post1 = firstfour[0]
	post2 = firstfour[1]
	post3 = firstfour[2]
	post4 = firstfour[3]
	return render(request, 'new.html', {"post1" : post1,"post2" : post2,"post3" : post3,"post4" : post4})

def Archive(request):
	posts = Post.objects.order_by("-upload_date")
	return render(request, 'archive.html', {"posts" : posts})

def AboutUs(request):
	context = {}
	firstfour = Featured_Product.objects.order_by("-upload_date")[:4]
	prod1 = firstfour[0]
	prod2 = firstfour[1]
	prod3 = firstfour[2]
	prod4 = firstfour[3]
	return render(request, 'about_us.html', {"prod1" : prod1, "prod2" : prod2, "prod3" : prod3, "prod4" : prod4})

def Products(request):
	air = Air_Filter.objects.all()
	water = Water_Filter.objects.all()
	dust = Dust_Filter.objects.all()
	services = Service.objects.all()
	return render(request, 'products.html', {"air_filters" : air, "water_filters" : water, "dust_filters" : dust, "services" : services})

def OpenTab(request, filter_name):
	air = Air_Filter.objects.all()
	water = Water_Filter.objects.all()
	dust = Dust_Filter.objects.all()
	objlist = []
	for x in air:
		if str(x.name) == str(filter_name):
			objlist.append(x)
			return render(request,'prod.html',{'item': objlist[0]})
	for y in water:
		if str(y.name) == str(filter_name):
			objlist.append(y)
			return render(request,'prod.html',{'item': objlist[0]})
	for z in dust:
		if str(z.name) == str(filter_name):
			objlist.append(z)
			return render(request,'prod.html',{'item': objlist[0]})
def OpenService(request, service_name):
	services = Service.objects.all()
	objlist = []
	for x in services:
		if str(x.name) == str(service_name):
			objlist.append(x)
			return render(request,'service.html', {"service" : objlist[0]})

def Search(request):
	air = Air_Filter.objects.all()
	water = Water_Filter.objects.all()
	dust = Dust_Filter.objects.all()
	if request.method == 'POST':
		search = SearchBox(request.POST)
		if search.is_valid():
			objlist = []
			search_string = search.cleaned_data['search']
			for x in air:
				if str(search_string.lower()) in str(x.name.lower()):
					objlist.append(x)
			for y in water:
				if str(search_string.lower()) in str(y.name.lower()):
					objlist.append(y)
			for z in dust:
				if str(search_string.lower()) in str(z.name.lower()):
					objlist.append(z)
			return render(request, 'search.html', {'objlist' : objlist, 'len' : len(objlist)})
		else:
			return render(request, 'products.html', {"air_filters" : air, "water_filters" : water, "dust_filters" : dust})

	return render(request, 'products.html', {"air_filters" : air, "water_filters" : water, "dust_filters" : dust})

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
				send_mail("Website Message", fullemail, settings.EMAIL_HOST_USER, ['ghii@ghii.com.ph '], fail_silently=False)
				return render(request, 'contact_us.html', context)
			except:
				return render(request, 'contact_us.html', context)
		else:
			return render(request, 'contact_us.html', context)
	else:
		return render(request, 'contact_us.html', context)

