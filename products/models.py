from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

    
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_1_thumbnail = ImageSpecField(source='image_1', processors=[ResizeToFit(300, 300)], format='JPEG', options={'quality': 90})
    image_2_thumbnail = ImageSpecField(source='image_2', processors=[ResizeToFit(300, 300)], format='JPEG', options={'quality': 90})
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name