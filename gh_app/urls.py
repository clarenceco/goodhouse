from django.conf.urls import url
from gh_app import views
from views import *

urlpatterns = [
	url(r'^$', HomePage, name = 'HomePage'),
	url(r'^aboutus/', AboutUs, name = 'AboutUs'),
	url(r'^contactus/', ContactUs, name = 'ContactUs'),
	url(r'^careers/', Careers, name = 'Careers'),
	url(r'^products/', Products, name = 'Products'),
]
