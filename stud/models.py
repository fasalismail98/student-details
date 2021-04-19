from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    type = models.CharField(max_length=200, null=True)

class stud(models.Model):
    name=models.CharField(max_length=100,null=True)
    id=models.IntegerField(primary_key=True)
    age=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
    mark=models.IntegerField(null=True)
    image=models.ImageField(upload_to='images/')



