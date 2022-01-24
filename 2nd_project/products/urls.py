from django.urls import path
from . import views

urlpatterns = [
    path('',views.products,name='products'),
    path('prodect/',views.product,name='product'),    
]