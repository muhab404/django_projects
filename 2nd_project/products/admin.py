from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'active', 'category']
    list_display_links = ['price', 'name']
    list_editable = ['category']
    search_fields = ['name']
    list_filter = ['category', 'price'] 

admin.site.register(Product,ProductAdmin)