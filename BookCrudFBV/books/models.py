from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

