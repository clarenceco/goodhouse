from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime

class Post(models.Model):
	title = models.CharField(max_length = 100, primary_key = True)
	text = models.TextField()
	docfile = models.FileField(upload_to = 'Posts/Year: %Y/Month: %m/Day: %d', default = 'NULL.jpg')
	
	def __str__(self):
		return self.title

class Category1_Product(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	docfile = models.FileField(upload_to = 'Category1_Products/', default = 'NULL.jpg')

	def __str__(self):
		return self.name

class Category2_Product(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	docfile = models.FileField(upload_to = 'Category2_Products/', default = 'NULL.jpg')

	def __str__(self):
		return self.name

class Category3_Product(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	docfile = models.FileField(upload_to = 'Category3_Products/', default = 'NULL.jpg')

	def __str__(self):
		return self.name

class Category4_Product(models.Model):
	name = models.CharField(max_length = 100, primary_key = True)
	description = models.TextField()
	docfile = models.FileField(upload_to = 'Category4_Products/', default = 'NULL.jpg')

	def __str__(self):
		return self.name