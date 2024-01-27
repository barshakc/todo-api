from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class TimeStampedModel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)


class ToDo(TimeStampedModel):
    STATUS_CHOICES = [
        ('todo', 'To do'),
        ('in_progress', 'In progress'),
        ('completed', 'Completed'),
    ]

    title=models.CharField(max_length=255)
    description=models.TextField()
    due_date=models.DateField()
    status=models.CharField(max_length=255,choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
