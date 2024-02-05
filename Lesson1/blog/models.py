from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Shop(models.Model):
    item = models.CharField(max_length=20)
    quantity = models.IntegerField
    price = models.IntegerField
