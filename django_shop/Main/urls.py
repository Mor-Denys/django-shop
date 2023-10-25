from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_url'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category_url'),
    path('order_save', order_save)
]