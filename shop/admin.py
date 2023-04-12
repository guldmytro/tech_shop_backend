from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated',)
    list_filter = ('available', 'created', 'updated',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created',)
