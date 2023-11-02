from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

    
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    image_1_thumbnail = ImageSpecField(source='image_1', 
                                       processors=[ResizeToFit(600, 400)],
                                       format='JPEG', options={'quality': 60})
    image_2_thumbnail = ImageSpecField(source='image_2',
                                       processors=[ResizeToFit(600, 400)], 
                                       format='JPEG', options={'quality': 60})
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    @property
    def Imageurl(self):
        try:
            url=self.image_1_thumbnail.url
        except:
            url=''

                
        return url

    @property
    def Imageurl2(self):
        try:
            url=self.image_2_thumbnail.url
        except:
            url=''

                
        return url