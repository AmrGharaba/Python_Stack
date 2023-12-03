from django.db import models
import re

class usermanager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_address']): 
            errors['email_address'] = "Invalid email address!"
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'first name must be two characters minimum'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'last name must be at least two characters'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'passwords must match'
        if len(postData['password']) < 8:
            errors['password_length'] = 'password must be at least eight characters long'
        return errors

class bookmanager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['title']) < 1 :
            errors['title'] = 'Title is required'
        if len(postData['desc']) < 5:
            errors['desc'] = 'Description must be atleast 5 characters long'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length = 45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = usermanager()
    
class Book(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fav_users = models.ManyToManyField(User, related_name='fav_books')
    my_user = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE )
    objects = bookmanager()

# Create your models here.
