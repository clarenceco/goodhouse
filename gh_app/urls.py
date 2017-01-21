from django.conf.urls import url
from gh_app import views
from views import *

urlpatterns = [
	url(r'^$', AboutUs, name = 'New'),
	url(r'^new/', New, name = 'New'),
	url(r'^archive/', Archive, name = 'Archive'),
	url(r'^aboutus/', AboutUs, name = 'AboutUs'),
	url(r'^products/', Products, name = 'Products'),
	url(r'^careers/', Careers, name = 'Careers'),
	url(r'^contactus/', ContactUs, name = 'ContactUs'),
	url(r'^send/', Send, name = 'Send'),
	url(r'^opentab/(?P<filter_name>[\w|\W]+)/$', OpenTab, name = 'OpenTab'),
	url(r'^search/(?P<search_string>[\w|\W]+)/$', Search, name = 'Search'),
]
