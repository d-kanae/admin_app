# import site
from msilib.schema import AdminUISequence, Class
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .models import *



class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_app_date")
    search_fields = ("customer_name", "customer_app_date")
    list_filter = ["customer_name"]

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("products_name", "best_before_duration", "product_app_date")
    search_fields = ("products_name", "best_before_duration")
    list_filter = ["products_name"]
    list_per_page = 30
    list_max_show_all = 20000

class ProductionAdmin(admin.ModelAdmin):
    list_display = ("products_name", "production_date", "production_volume")
    search_fields = ("products_name", "production_volume")
    list_filter = ["products_name"]
    date_hierarchy = "production_date"
    
    def products_name(self, obj):
        return obj.products_name
    products_name.short_description = '商品名'
    products_name.admin_order_field = 'products_name'

class SaleAdmin(admin.ModelAdmin):
    list_display = ("products_name", "production_date", "customer_name", "sale_date", "sale_volume")
    search_fields = ("products_name", "production_date", "sale_volume")
    list_filter = ["products_name", "customer_name"]
    date_hierarchy = "sale_date"
    list_per_page = 30
    list_max_show_all = 20000
    
    def bbdate(self):
        best_before_date = self.production_date + self.best_before_duration
        return best_before_date

admin.site.register(Products, ProductsAdmin)
admin.site.register(Production, ProductionAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sale, SaleAdmin)

