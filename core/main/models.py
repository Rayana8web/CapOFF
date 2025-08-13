from django.db import models
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title



class Size(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Brand(models.Model):
    title = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title



#class ProductBrand(models.Model):
  #  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  #  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)



class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)



class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)



#class BasketItems(models.Model):
  #  basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
  #  storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
  #  quantity = models.PositiveIntegerField(default=1)
  # created_at = models.DateTimeField(auto_now_add=True)



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, default='pending')


#class OrderItems(models.Model):
  #  order = models.ForeignKey(Order, on_delete=models.CASCADE)
   # storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
   # quantity = models.PositiveIntegerField(default=1)



class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
