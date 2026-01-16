from django.db import models
from django.utils import timezone

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(null=True)
    avatar = models.ImageField()
    date_created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title