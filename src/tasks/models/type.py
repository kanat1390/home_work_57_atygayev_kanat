from random import choices
from django.db import models

class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=40)

    def __str__(self):
        return self.name