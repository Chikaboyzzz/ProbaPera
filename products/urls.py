from products import views
from .views import product_list

from django.contrib import admin
from django.urls import path,include
from products import views


app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # path('create/', views.ProductCreateView.as_view(), name='create'),
    
]
