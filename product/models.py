from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва категорії")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Слаг")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва продукту")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Слаг")
    price = models.FloatField(verbose_name="Ціна")
    product_qty = models.IntegerField(verbose_name="Кількість товару")
    reviews_qty = models.IntegerField(verbose_name="Кількість відгуків")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} : {self.price}$"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})