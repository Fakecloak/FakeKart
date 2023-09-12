"""
URL configuration for FakeProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from FakeKart import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('collections/',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_view,name="product_view"),
    path('login',views.login_page,name="login"),
    path('logout',views.logout_page,name="logout"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('cart',views.cart_page,name="cart"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage',views.favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('checkout',views.checkout_page,name="checkout"),
    #footer urls
    path('Affiliate',views.Affiliate,name="Affiliate"),
    path('sell_on',views.sell_on,name="sell_on"),
    path('advertise',views.advertise,name="advertise"),
    path('FAQ',views.FAQ,name="FAQ"),
    path('Feedback',views.Feedback,name="Feedback"),
    path('About_us',views.About_us,name="About_us"),
    path('contact',views.Contact,name="contact"),
]

