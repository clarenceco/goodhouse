from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
	title = models.CharField(max_length = 100, primary_key = True)
	text = models.TextField()
	docfile1 = models.FileField(upload_to = 'Posts/Year: %Y/Month: %m/Day: %d', default = '')
	docfile2 = models.FileField(upload_to = 'Posts/Year: %Y/Month: %m/Day: %d', default = '')
	docfile3 = models.FileField(upload_to = 'Posts/Year: %Y/Month: %m/Day: %d', default = '')
	docfile4 = models.FileField(upload_to = 'Posts/Year: %Y/Month: %m/Day: %d', default = '')
	docfile5 = models.FileField(upload_to = 'Posts/Year: %Y/Month: %m/Day: %d', default = '')
	
	def __str__(self):
		return self.title

class AirWater_Filter(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	docfile1 = models.FileField(upload_to = 'AirWater_Filters/', default = '')
	docfile2 = models.FileField(upload_to = 'AirWater_Filters/', default = '')
	docfile3 = models.FileField(upload_to = 'AirWater_Filters/', default = '')
	docfile4 = models.FileField(upload_to = 'AirWater_Filters/', default = '')
	docfile5 = models.FileField(upload_to = 'AirWater_Filters/', default = '')

	def __str__(self):
		return self.name

class AirWater_EquipmentConsumable(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	docfile1 = models.FileField(upload_to = 'AirWater_EquipmentConsumables/', default = '')
	docfile2 = models.FileField(upload_to = 'AirWater_EquipmentConsumables/', default = '')
	docfile3 = models.FileField(upload_to = 'AirWater_EquipmentConsumables/', default = '')
	docfile4 = models.FileField(upload_to = 'AirWater_EquipmentConsumables/', default = '')
	docfile5 = models.FileField(upload_to = 'AirWater_EquipmentConsumables/', default = '')

	def __str__(self):
		return self.name