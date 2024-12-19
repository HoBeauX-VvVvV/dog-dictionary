from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Dogs(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dog-detail', kwargs={'dog_id': self.id})