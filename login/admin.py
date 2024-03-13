from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Custmor)
admin.site.register(models.Order)
admin.site.register(models.Orderitem)
admin.site.register(models.Product)
admin.site.register(models.shippingadress)
admin.site.register(models.Shop)