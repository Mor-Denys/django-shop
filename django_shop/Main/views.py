from django.shortcuts import render
from django.db.models import Q
from .models import *
from django.views.generic import ListView, DetailView
from .utils import CotagoriesMixin


class HomeView(ListView, CotagoriesMixin):
    model = Product

    def get_queryset(self):
        user_request = self.request.GET.get('search', None)

        if user_request:
            return self.model.objects.filter(
                Q(name__icontains=user_request)
                |
                Q(description__icontains=user_request)
            )
        return self.model.objects.all()


class ProductView(DetailView, CotagoriesMixin):
    model = Product


class CategoryView(DetailView, CotagoriesMixin):
    model = Category


def order_save(request):
    сategories = Category.objects.all()
    order = Order()
    order.name = request.POST['username']
    order.email = request.POST['user_gmail']
    order.product = Product.objects.get(pk=request.POST['product_id'])
    order.save()
    return render(
        request,
        'Main/order.html',
        {
            'categories': сategories,
            'order': order
        }
    )
