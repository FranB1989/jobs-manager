from django.db import models
from applications.models import Application
from calendars.models import Calendar

# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default=None, blank=True, null=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='jobs', null=True, blank=True)

    def __str__(self):
        return f"Job: {self.name}, Type: {self.type}, Status: {self.status}"
