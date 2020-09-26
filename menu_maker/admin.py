from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("product","cut_details", "rate", "availability")
    ordering = ('product', )
    search_fields = ('product', )
    