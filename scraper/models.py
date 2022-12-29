from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Name_Cheap(models.Model):
    url = models.CharField(default="", max_length=10000)


    def __str__(self):
        return f'{self.url}'


class Domain(models.Model):
    url = models.CharField(default="", max_length=10000)


    def __str__(self):
        return f'{self.url}'

class Hover(models.Model):
    url = models.CharField(default="", max_length=10000)


    def __str__(self):
        return f'{self.url}'
