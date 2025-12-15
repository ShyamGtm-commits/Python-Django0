from django.db import models

# Create your models here.
class Expenditure(models.Model):
    title = models.CharField(max_length=30)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=20)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
