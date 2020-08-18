from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exp(models.Model):
    text = models.CharField(max_length=260)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "{}-{}".format(self.amount, self.date)


class Income(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    def __unicode__(self):
        return "{}-{}".format(self.amount, self.date)
