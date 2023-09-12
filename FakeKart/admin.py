from django.contrib import admin
from .models import *
# Register your models here.
"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','images','description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','product_images','description')

"""
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Cart)