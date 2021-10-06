from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    level = models.IntegerField()

    def __str__(self):
        return self.name
