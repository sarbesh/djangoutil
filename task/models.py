from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
    ('started', 'Started'),
    ('completed', 'Completed'),
    ('progress', 'Progress'),
    ('failed', 'Failed'),
)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250, blank=True, default='')
    status = models.CharField(max_length=10, blank=False, choices=STATUS_CHOICES, default='Started')
    report = models.URLField(blank=True)
    pushNotification = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return "name : {}, status : {} , owner : {}".format(self.name, self.status, self.owner)
