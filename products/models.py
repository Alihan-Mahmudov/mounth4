from django.db import models

# Create your models here.

class Category(models.Model):
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=50)

class Product(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length = 50)
    description = models.TextField()
    rate = models.FloatField()
    post_date = models.DateTimeField(auto_now_add =True)

class Review(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add =True)
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
