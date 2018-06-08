from django.db import models

# Create your models here.
# Creating objects for the database.
class ArtWork(models.Model):
    image = models.ImageField(upload_to='images/') #image for the picture
    desc = models.CharField(max_length=200) #this is a descripton of the image
    title = models.CharField(max_length=30,default="Title")
                          
                          
