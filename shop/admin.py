from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin)
    list_display = ('title', 'slug', 'created', 'updated', 'body')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created',)
