from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=255,blank=True)
    description=models.TextField(max_length=255)
    image=models.ImageField(upload_to='products')
    price=models.IntegerField()
    
    def __str__ (self):
        return self.name