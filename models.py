from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
    class Issue(models.Model):
        summary = models.CharField(max_lenght=512)
        description = models.TextField()
        reportet = models.ForeignKey(
            get_user_model(),
            on_delete=models.CASCADE
        )
        assignee = models.