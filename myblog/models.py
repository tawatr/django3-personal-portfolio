from django.db import models

# Create your models here.
class myBlog(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='myblog/images/')
    date = models.DateField(null=True)
    url = models.URLField(blank=True)
