from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CHOICES = [
    ('PENDING', 'pending'),
    ('COMPLETED', 'completed'),
    ('UNCOMPLETE', 'uncomplete')
]

class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Task(TimeStampedMixin):
    task_sumary = models.CharField(max_length=100)
    task_deatil = models.TextField(max_length=250)
    task_dadline = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='Task')
    task_status = models.CharField(
        max_length=200,
        choices=CHOICES,
        default='pending',
    )

    def __str__(self):
        return self.task_sumary
