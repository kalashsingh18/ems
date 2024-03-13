from django.contrib import admin
from django.urls import path
from login import views


urlpatterns = [
    
    path("login",views.sign,name="sign"),
    path("confirmation",views.confirmation,name="confirmation"),
    path("signin",views.signin,name="signin"),
    path("home",views.home,name="home"),
    path("",views.store,name="store"),
    path("cart",views.cart,name="cart"),
    path("checkout",views.checkout,name="checkout"),
    path("ordertracking",views.ordertracking,name="tracking"),
    path("about",views.about,name="about"),
    path("offlineshop",views.offlineshop,name="offlineshop"),
    path("Createshop",views.createshop,name="createshop.html"),
    path("shopcreated",views.shopcreated,name="shopcreated"),
    path("searchshop",views.searchshop,name="searchshop"),
    path("order_tracking",views.searchshop,name="searchshop")

    
]