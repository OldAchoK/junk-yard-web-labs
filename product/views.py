from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import Category, Product
from .forms import CategoryForm, ProductForm

def home(request):
    categories_count = Category.objects.count()
    products_count = Product.objects.count()
    recent_products = Product.objects.all()[:5]
    
    context = {
        'categories_count': categories_count,
        'products_count': products_count,
        'recent_products': recent_products,
    }
    return render(request, 'product/home.html', context)

# Category Views
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'product/category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'product/category_detail.html', {
        'category': category,
        'products': products
    })

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категорію успішно створено!')
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'product/create_category.html', {'form': form})

def update_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категорію успішно оновлено!')
            return redirect('category-detail', slug=category.slug)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'product/update_category.html', {'form': form, 'category': category})

def delete_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Категорію успішно видалено!')
        return redirect('categories')
    return render(request, 'product/delete_category.html', {'category': category})

# Product Views
class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успішно створено!')
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'product/create_product.html', {'form': form})

def update_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успішно оновлено!')
            return redirect('product-detail', slug=product.slug)
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/update_product.html', {'form': form, 'product': product})

def delete_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Продукт успішно видалено!')
        return redirect('products')
    return render(request, 'product/delete_product.html', {'product': product})