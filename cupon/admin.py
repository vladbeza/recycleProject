from django.contrib import admin
from .models import Cupon

class CuponAdmin(admin.ModelAdmin):
    list_display = ["code", "active_from", "active_to", "discount", "is_active"]
    list_filter = ["active_from", "active_to", "is_active"]
    search_fields = ["code"]

admin.site.register(Cupon, CuponAdmin)