from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category= models.CharField(max_length = 150)
    
class post(models.Model):
    title= models.CharField(max_length = 150)
    content= models.TextField()
    img=models.ImageField()
    slug=models.SlugField(max_length = 50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
class comments(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE)
    comment=models.TextField() 
  

    
