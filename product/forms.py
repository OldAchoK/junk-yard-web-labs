from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введіть назву категорії',
                'class': 'form-control'
            })
        }
        labels = {
            'title': 'Назва категорії'
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'product_qty', 'reviews_qty', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Назва продукту',
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Ціна',
                'class': 'form-control',
                'step': '0.01'
            }),
            'product_qty': forms.NumberInput(attrs={
                'placeholder': 'Кількість товару',
                'class': 'form-control'
            }),
            'reviews_qty': forms.NumberInput(attrs={
                'placeholder': 'Кількість відгуків',
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'title': 'Назва продукту',
            'price': 'Ціна',
            'product_qty': 'Кількість товару',
            'reviews_qty': 'Кількість відгуків',
            'category': 'Категорія'
        }