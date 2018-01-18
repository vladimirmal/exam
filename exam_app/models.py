from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Categories, to_field='title', related_name='category', )

    def __str__(self):
        return self.title


class ElementsBasket(models.Model):
    user = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)
    number = models.IntegerField()
    product = models.ForeignKey(Products, to_field='title', )
    cost = models.DecimalField(decimal_places=2, max_digits=8, )

    def __str__(self):
        return self.product.title


class ProductVersion(models.Model):
    base_product = models.ForeignKey(Products, to_field='title', related_name='version')
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    cost = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.title


class Basket(models.Model):
    user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    elements = models.ForeignKey(ProductVersion, to_field='title', related_name='version')
    number = models.IntegerField()
    cost = models.DecimalField(decimal_places=2, max_digits=8)
    buy = models.BooleanField(default=False)


class Order(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=150)
    date_time = models.DateTimeField()
    product = models.ForeignKey(Basket)


class Profile(models.Model):
    user = models.ForeignKey(User)
    history = models.ForeignKey(Order)




# Create your models here.
