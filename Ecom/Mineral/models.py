from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Customer(models.Model):

    name = models.OneToOneField(User)
    website = models.URLField(blank=True)
    product = models.CharField(max_length=100,blank=True)
    product_image = models.ImageField(blank=True,upload_to="product_pics")


    def __str__(self):
        return self.name.username





