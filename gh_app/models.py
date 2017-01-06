from __future__ import unicode_literals
from django.db import models
from django import forms
from cloudinary.models import CloudinaryField
from django.utils import timezone
import datetime


class Post(models.Model):
	title = models.CharField(max_length = 100, primary_key = True)
	text = models.TextField()
	image_file = CloudinaryField('image', blank=True, null=True)
	video_URL = models.CharField(max_length = 200, blank=True)
	image_exists = models.BooleanField()
	video_exists = models.BooleanField()
	upload_date = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.title

class AirWater_Filter(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	file = CloudinaryField('image')
	upload_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.name

class AirWater_EquipmentConsumable(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	file = CloudinaryField('image')
	upload_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.name

class Career(models.Model):
	title = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	upload_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.title

class ContactForm(forms.Form):
    contact = forms.CharField(required=True)
    content = forms.CharField(required=True)