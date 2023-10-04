from django.contrib.auth.models import get_user_model
from django.db import models
from django.urls import reverse


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_lenght=128)
    description =models.CharField(max_lenght=256)
    
    def __str__(self):
        return self.name
    
class Issue(models.model):
    summary = models.CharField(max_length=512)  
    descritption = models.TextField()
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee",
        blank=True, null=True
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee",
        blank=True, null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.summary[:256]   
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])
     