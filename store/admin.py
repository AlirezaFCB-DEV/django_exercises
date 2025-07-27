from django.contrib import admin
from .models import Product
# Register your models here.

# admin.site.register(Product)
@admin.register(Product)
class Product_Admin (admin.ModelAdmin):
    list_display= ("name" , "price" , "in_stock" , "created_at")
    list_filter = ("in_stock",)
    search_fields = ("name" ,)