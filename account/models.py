from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.9
class CustomUser(AbstractUser):
    phone=models.CharField(max_length=20)

