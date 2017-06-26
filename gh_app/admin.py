from __future__ import unicode_literals 
from django.contrib import admin
from .models import Post, Air_Filter, Water_Filter, Dust_Filter, Featured_Product, Career, Service, ProductCatalog

admin.site.register(Post)
admin.site.register(Career)
admin.site.register(Air_Filter)
admin.site.register(Water_Filter)
admin.site.register(Dust_Filter)
admin.site.register(Service)
admin.site.register(Featured_Product)
admin.site.register(ProductCatalog)
# Register your models here.
