from django.db import models
from djrichtextfield.models import RichTextField
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering =['-create_at']
    
    def __str__(self):
        return self.title
    
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="books", on_delete=models.CASCADE)
    ispn = models.CharField(max_length=20)
    pages = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
    description = RichTextField()
    imageurl = models.URLField()
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-create_at']
        
    def __str__(self):
        return self.title
    

class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    imageurl = models.URLField()
    status = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering =['-create_at']
        
    def __str__(self):
        return self.name    