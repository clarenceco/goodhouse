from __future__ import unicode_literals 
from django.contrib import admin
from .models import Post, AirWater_Filter, AirWater_EquipmentConsumable, Featured_Product, Career

admin.site.register(Post)
admin.site.register(Career)
admin.site.register(AirWater_Filter)
admin.site.register(AirWater_EquipmentConsumable)
admin.site.register(Featured_Product)
# Register your models here.
