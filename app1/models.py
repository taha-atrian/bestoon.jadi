from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exp(models.Model):
    text = models.CharField(max_length=260)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="")


