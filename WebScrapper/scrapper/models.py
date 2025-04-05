from django.db import models
 
# Create your models here.
class Link(models.Model):
 

    address = models.CharField(max_length=1000,default='no_link')
    name = models.CharField(max_length=1000,default='no_name')

    def __str__(self):    
       return self.name if self.name else "Unnamed Link"
 
