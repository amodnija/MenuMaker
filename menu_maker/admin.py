from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("product", "net_wt", "availability")
    ordering = ('product', )
    search_fields = ('product', )
    