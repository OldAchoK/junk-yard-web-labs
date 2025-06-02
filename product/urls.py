from django.urls import path
from .views import (
    home, category_list, category_detail, create_category, update_category, delete_category,
    ProductListView, product_detail, create_product, update_product, delete_product
)

urlpatterns = [
    path('', home, name='home'),
    
    # Category URLs
    path('categories/', category_list, name='categories'),
    path('categories/create/', create_category, name='category-create'),
    path('categories/<slug:slug>/', category_detail, name='category-detail'),
    path('categories/<slug:slug>/update/', update_category, name='category-update'),
    path('categories/<slug:slug>/delete/', delete_category, name='category-delete'),
    
    # Product URLs
    path('products/', ProductListView.as_view(), name='products'),
    path('products/create/', create_product, name='product-create'),
    path('products/<slug:slug>/', product_detail, name='product-detail'),
    path('products/<slug:slug>/update/', update_product, name='product-update'),
    path('products/<slug:slug>/delete/', delete_product, name='product-delete'),
]