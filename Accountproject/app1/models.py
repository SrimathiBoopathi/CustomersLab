from django.db import models


# Create your models here

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.CharField(max_length=100, unique=True)
    account_name = models.CharField(max_length=100)
    app_secret_token = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.account_name


