from django.shortcuts import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return HttpResponse(products)