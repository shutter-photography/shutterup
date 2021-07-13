from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class POST(models.Model):
    Name = models.CharField(max_length=200,unique=True)
    new_image = models.ImageField(upload_to='posts/images/',blank=True)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.Name



class UPDATE(models.Model):
    Title = models.CharField(max_length=30)
    new_update = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.Title
