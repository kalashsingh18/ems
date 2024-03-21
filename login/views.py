from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Product,Orderitem,Order,shippingadress,Shop
def sign(request):
    return render(request,"login.html")
def confirmation(request):
    if request.method=='POST':
     names=request.POST.get('name')
     
     passwords=request.POST.get('password')
     emails=request.POST.get('email')
     print(filter(names))
     if filter(names) and filterp(passwords):
         user1=User(name=names,password=passwords,email=emails)
         user1.save()
         return render(request,"confirmation.html")
     if filterp(passwords)==False:
         return HttpResponse("not valid password may contain an special character")

     else:
        return HttpResponse("invalid name")

     
     
def filter(names):
    x=0
    for i in names:
        if 122>ord(i)>65:
            print(ord(i))
            x=x+1
            if x==len(names)-1:
                return True
            continue
          
        else:
            return False
def filterp(passwords):
   x="@!#$"
   y=0
   for i in x :
       if i in passwords:
           y=y+1
           print("y",y)
           continue
   if y==0:
       return False
   else:
       return True
def signin(request):
    return render(request,"signup.html")
def home(request):
    names=request.POST.get("name")
    print(names)
    passwords=request.POST.get("password")
    print(passwords)
    data_exists = User.objects.filter(name=names).values()
    x=0
    for i in data_exists:
        if  i["name"]==names and i["password"]==passwords:
            request="homepage"
            return request
            x=x+1
    return HttpResponse("not the user")
def store(request):
    products=Product.objects.all()
    x=[]
    for i in products:
        i=str(i)
        p="image/"+i
        x.append(p)
    context={"product":products,"modify":x}
    return render(request,"store.html",context)
def cart(request):
   x=Orderitem.objects.all().values()
   y=Product.objects.all().values()
   z=[]
   print(x)
   w=[]
   
   for j in x:
  
    for  i in y:
           if j["product_id"]==i["id"]:
               z.append(i)
               i["quantity"]=j["quantity"]
               i["total"]=i["quantity"]*i["price"]
               i["image"]="images/"+i["image"]
               
              
  
   print(z)
    
   return render(request,"cart.html",{"items":z})
def checkout(request):
   x=Orderitem.objects.all().values()
   y=Product.objects.all().values()
   z=[]
   print(x)
   w=[]
   
   for j in x:
  
    for  i in y:
           if j["product_id"]==i["id"]:
               z.append(i)
               i["quantity"]=j["quantity"]
               i["total"]=i["quantity"]*i["price"]
               i["image"]="images/"+i["image"]
               
              
  
   print(z)
    
   
   return render(request,"checkout.html",{"items":z})
def ordertracking(request):
    names=request.GET.get("name")
    adress=request.GET.get("address" )
    gmail=request.GET.get("email")
    zipcode=request.GET.get("zipcode")
    userquery=User.objects.all().values()
    if check(userquery,names,gmail):
        return render(request,"ordertracking.html")
    else:
        return HttpResponse("soory you are not the user")
    print(userquery)

    return render(request,"ordertracking.html")
def check(userquery,names,gmail):
    for i in userquery:
        if i["name"]==names and i["email"]==gmail:
            return True
        
    else:
        False
def about(request):
    return render(request,"about.html")
def offlineshop(request):
    return render(request,"offlineshop.html")
def createshop(request):
    return render(request,"createshop.html")
from django.http import HttpResponse
from .models import Shop  # Import your Shop model

def shopcreated(request):
    if request.method == "POST":
        username = request.POST.get("username")
        longitude = request.POST.get("longitude")
        latitude = request.POST.get("latitude")
        password = request.POST.get("password")
        products = request.POST.get("products")
        shop_name = request.POST.get("shopName")
        try:
            longitude = float(longitude)
            latitude = float(latitude)
        except (TypeError, ValueError):
            return HttpResponse("Invalid longitude or latitude value")
        
        # Create a new Shop instance with the provided data
        new_shop = Shop(
            username=username,
            password=password,
            longitude=longitude,
            latitude=latitude,
            products=products,
            shop_name=shop_name
        )
        
        # Save the new shop to the database
        new_shop.save()
        
        # Optionally, you can return a success message
        return render(request,"congratulations.html")
    else:
        # Handle other HTTP methods (e.g., GET)
        return HttpResponse("Only POST requests are allowed")
def searchshop(request):
    adress=request.POST.get("address")
    latitude=request.POST.get("latitude")
    longitude=request.POST.get("longitude")
    product=request.POST.get("product")
    print(product)
    product="bmw"
    
    print(latitude)
    queryset=Shop.objects.all().values()
    x=[]
    p=""
    for i in queryset:
        x.append(i)
    for i in x:
              if i["products"] == product:
                firstlongitude=str(longitude)
                firstlatitude=str(latitude)
                secoundlongtitude=str(i['longitude'])
                secoundlatitude=str(i['latitude'])
                x="https://www.google.com/maps/dir/22.1694672,76.8426563/22.6721792,75.8317056"
                y="/data=w"
                first=firstlongitude+firstlatitude
                secound=secoundlongtitude+secoundlatitude
                final=x+first+'/'+secound+y
                print(final)
                
                return render(request,"finallyyy.html",{"finals":final})
    return HttpResponse(queryset)
def view(request):
    product=request.POST.get("product")
    return render(request,"views.html",{"products":product})
      
           
           
    

        

        
        
 
       
       
   


# Create your views here.
