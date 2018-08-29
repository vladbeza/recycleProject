from django.contrib import admin
from .models import *
# Register your models here.

class ProductsInline(admin.StackedInline):
    model = Product
    extra = 3

class CategotyAdmin(admin.ModelAdmin):
    inlines = [ProductsInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "added_date", "price", "count", "color", "image"]
    list_filter = ["product_name", "added_date", "price", "count"]
    list_editable = ["price", "count", "image"]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)