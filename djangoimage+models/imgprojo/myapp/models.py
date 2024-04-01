from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    video = models.FileField(upload_to='media', blank=True, null=True)
