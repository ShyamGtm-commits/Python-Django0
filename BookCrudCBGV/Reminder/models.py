from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),

    ]

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICES ,default='pending')
    banner = models.ImageField(default='fallback.png', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return self.title
    

