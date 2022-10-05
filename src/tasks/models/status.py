from django.db import models

class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    color = models.CharField(verbose_name='Цвет', max_length=7)

    def __str__(self):
        return self.name