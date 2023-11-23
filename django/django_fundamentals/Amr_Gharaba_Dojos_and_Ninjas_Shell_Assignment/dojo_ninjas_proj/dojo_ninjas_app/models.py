from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length = 45)
    city = models.CharField(max_length = 45)
    state = models.CharField(max_length = 45)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
# ninjas is the foreign key in Ninja for Dojo

class Ninja(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    dojo = models.ForeignKey(Dojo, related_name='ninjas',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


# Create your models here.
