from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
	title = models.CharField(max_length = 100, primary_key = True)
	text = models.TextField()
	image_file = models.FileField(upload_to = 'Posts/Year: %Y/Month: %m/Day: %d', default = 'gh.png')
	video_file = models.FileField(upload_to = 'Posts/Year: %Y/Month: %m/Day: %d', blank = True )
	video_exists = models.BooleanField()
	upload_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.title

class AirWater_Filter(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	file = models.FileField(upload_to = 'AirWater_Filters/')
	upload_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.name

class AirWater_EquipmentConsumable(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	file = models.FileField(upload_to = 'AirWater_EquipmentConsumables/')
	upload_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.name

class Career(models.Model):
	title = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	upload_date = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return self.title