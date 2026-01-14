from django.db import models
from django.utils import timezone

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to= "blogs_image/")
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
