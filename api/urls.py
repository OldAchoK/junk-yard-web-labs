from django.urls import path, include
from tastypie.api import Api
from .resources import CategoryResource, ProductResource

v1_api = Api(api_name='v1')
v1_api.register(CategoryResource())
v1_api.register(ProductResource())

app_name = 'api'

urlpatterns = [
    path('', include(v1_api.urls)),
]
