from django.db import models
from app1.models import Account

# Create your models here.

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='destinations')
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()

    def __str__(self):
        return self.url
