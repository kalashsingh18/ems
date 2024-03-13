from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class User(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=1200)
    isauser=models.BooleanField(default=True)


class Custmor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=300,null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def imageurl(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
class Order(models.Model):
    custmor=models.ForeignKey(Custmor, null=True,blank=True, on_delete=models.SET_NULL)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=332,null=True)
    def __str__(self):
        return str(self.id)
class Orderitem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
class shippingadress(models.Model):
    custmor=models.ForeignKey(Custmor,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=300,default='')
    shiping_adress=models.CharField(max_length=300,default='')
    state=models.CharField(max_length=400,null=True)
    city=models.CharField(max_length=500,null=True)
    zipcode=models.CharField(max_length=400,null=True)
    data_added=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.adress
class Shop(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    products = models.TextField()
    shop_name = models.CharField(max_length=100)
    
    