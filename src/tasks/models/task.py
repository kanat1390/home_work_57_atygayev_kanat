from django.db import models


class Task(models.Model):
    summary = models.CharField(verbose_name='Заголовок', max_length=200)
    description = models.TextField(verbose_name='Описание', null=True, blank=True, max_length=2000)
    status = models.ForeignKey(verbose_name='Статус', to='tasks.Status', on_delete=models.PROTECT)
    type = models.ForeignKey(verbose_name='Тип', to='tasks.Type', on_delete=models.PROTECT) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary
