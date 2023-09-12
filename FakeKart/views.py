from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json
# Create your views here.


def home(request):
    products=Products.objects.filter(trending=1)
    return render(request, 'FakeKart/index.html',{'products':products})

def login_page(request):
    if request.user.is_authenticated:
        return  redirect("/")
    else:
        if request.method == 'POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successful")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password")
                return redirect("/login")
        return render(request, 'FakeKart/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logout successful")
    return redirect("/")
    


def register(request):
    form=CustomUserForm()
    if request.method == 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully Registered")
            return redirect('/login')
    return render(request, 'FakeKart/register.html',{'form':form})

def collections(request):
    category=Category.objects.filter(status=0)
    return render(request, 'FakeKart/collections.html',{'category':category})

def collectionsview(request,name):
    if (Category.objects.filter(name=name,status=0)):
        products=Products.objects.filter(category__name=name)
        return render(request, 'FakeKart/products/index.html',{'products':products,'name':name})
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')
    
def product_view(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Products.objects.filter(name=pname,status=0)):
            products=Products.objects.filter(name=pname,status=0).first()
            return render(request, 'FakeKart/products/product_view.html',{'products':products})
        else:
            messages.warning(request,"No Such Product Found")
            return redirect('collections')
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('collections')

def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      product_status=Products.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)         
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
   
def cart_page(request):
   if request.user.is_authenticated:
      cart=Cart.objects.filter(user=request.user)
      return render (request, "FakeKart/cart.html",{"cart":cart})
   else:
      return redirect("/")
   
def remove_cart(request,cid):
   cartitem=Cart.objects.get(id=cid)
   cartitem.delete()
   return redirect("/cart")

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']  
      product_status=Products.objects.get(id=product_id)
      if product_status:
        if Favorite.objects.filter(user=request.user.id,product_id=product_id):
           return JsonResponse({'status':'Product Already in Favorite'}, status=200)
        else:
            Favorite.objects.create(user=request.user,product_id=product_id)
            return JsonResponse({'status':'Product Added to Favorite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
   
def favviewpage(request):
   if request.user.is_authenticated:
      fav=Favorite.objects.filter(user=request.user)
      return render (request, "FakeKart/fav.html",{"fav":fav})
   else:
      return redirect("/")
   
def remove_fav(request,fid):
   item=Favorite.objects.get(id=fid)
   item.delete()
   return redirect("/favviewpage")

def checkout_page(request):
   return render(request, "FakeKart/checkout.html")

def Affiliate(request):
   return render(request, "FakeKart/footer/affiliate.html")

def sell_on(request):
   return render (request, "FakeKart/footer/sell_on.html")

def advertise(request):
   return render (request,"Fakekart/footer/advertise.html")

def FAQ(request):
   return render(request,"FakeKart/footer/FAQ.html")

def Feedback(request):
   return render(request,"FakeKart/footer/Feedback.html")

def About_us(request):
   return render(request,"FakeKart/footer/about_us.html")  

def Contact(request):
   return render(request,"FakeKart/footer/contact.html") 
