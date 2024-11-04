from django.db import models

class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    date_joined=models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

class Order(models.Model):
    user_name=models.ForeignKey(User, on_delete=models.CASCADE)
    product_name=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    order_date=models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField

class Review(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.ForeignKey(Product, on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    review_date=models.DateTimeField(auto_now_add=True)