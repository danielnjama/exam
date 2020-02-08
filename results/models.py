from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class final_results(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    percentage = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)

    class Meta:
        ordering =['-marks']

    def __str__(self):
        return self.name