from django.contrib import admin
from .models import Post, AirWater_Filter, AirWater_EquipmentConsumable, Career

admin.site.register(Post)
admin.site.register(Career)
admin.site.register(AirWater_Filter)
admin.site.register(AirWater_EquipmentConsumable)
# Register your models here.