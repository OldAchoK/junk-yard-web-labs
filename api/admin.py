from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at']
    ordering = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'product_qty', 'reviews_qty', 'created_at']
    list_filter = ['category', 'created_at', 'updated_at']
    search_fields = ['title', 'slug', 'category__title']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    list_select_related = ['category']
    
    # Add price range filter
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')