from django.db import models

# Create your models here.
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    product_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title + ' : ' + str(self.price) + '$'