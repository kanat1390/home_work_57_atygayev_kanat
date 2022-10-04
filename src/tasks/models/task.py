from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=2000)
    status = models.ForeignKey('tasks.Status', models.PROTECT)
    type = models.ForeignKey('tasks.Type', models.PROTECT) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.summary
