from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    list_editable = ['slug']
    list_filter = ['created_at']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'product_qty', 'reviews_qty', 'category', 'created_at']
    list_editable = ['price', 'product_qty', 'reviews_qty']
    list_filter = ['category', 'created_at', 'price']
    search_fields = ['title', 'category__title']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    list_per_page = 20
