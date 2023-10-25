from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_category_url(self):
        return reverse('category_url', kwargs={'pk': self.pk})


class Product(models.Model):
    image = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='product')

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('product_url', kwargs={'pk': self.pk})


class Order(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


