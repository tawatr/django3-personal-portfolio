from django.db import models

# Create your models here.
class myProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='myportfolio/images/')
    url = models.URLField(blank=True)

def __str__(self):
    return self.title
