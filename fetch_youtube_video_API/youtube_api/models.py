from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(null=True,blank=True,max_length=200)                              
    channelTitle = models.CharField(null=True,blank=True,max_length=100)                        
    description = models.CharField(null=True, blank=True, max_length=5000)                     
    publishingDateTime = models.DateTimeField()                                                 
    thumbnailsUrls = models.URLField()        