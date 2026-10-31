from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('title', 'description')
