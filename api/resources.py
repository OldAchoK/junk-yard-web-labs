from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from product.models import Category, Product


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']
        authentication = Authentication()
        authorization = Authorization()
        
        # Include all fields in JSON response
        fields = ['id', 'title', 'slug', 'created_at']
        
        # Enable filtering options
        filtering = {
            'title': ['exact', 'icontains', 'startswith'],
            'slug': ['exact'],
            'created_at': ['exact', 'range', 'gt', 'gte', 'lt', 'lte', 'year', 'month', 'day'],
        }
        
        # Set ordering options
        ordering = ['title', 'created_at', 'id']
        
        # Limit results per page
        limit = 20
        max_limit = 100


class ProductResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category', full=True)
    
    class Meta:
        queryset = Product.objects.select_related('category').all()
        resource_name = 'products'
        allowed_methods = ['get']
        authentication = Authentication()
        authorization = Authorization()
        
        # Include all fields in JSON response
        fields = [
            'id', 'title', 'slug', 'price', 'product_qty', 
            'reviews_qty', 'created_at', 'updated_at'
        ]
        
        # Enable extensive filtering options
        filtering = {
            'title': ['exact', 'icontains', 'startswith'],
            'slug': ['exact'],
            'price': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'product_qty': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'reviews_qty': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'category': ['exact'],
            'created_at': ['exact', 'range', 'gt', 'gte', 'lt', 'lte', 'year', 'month', 'day'],
            'updated_at': ['exact', 'range', 'gt', 'gte', 'lt', 'lte', 'year', 'month', 'day'],
        }
        
        # Set ordering options
        ordering = ['title', 'price', 'product_qty', 'reviews_qty', 'created_at', 'updated_at']
        
        # Limit results per page
        limit = 20
        max_limit = 50