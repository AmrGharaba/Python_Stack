from django.db import models


class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=100)
    release_date = models.DateTimeField(null=True)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
