from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Education(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    qualification=models.CharField(max_length=200)
    address=models.TextField(max_length=200)

