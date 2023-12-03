from django.db import models
import re

class Usemanager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_address']):    # test whether a field matches the pattern            
            errors['email_address'] = "Invalid email address!"
        if len(postData['password']) < 8:
            errors['password'] = 'passwrd should be at least eight characters'
        
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'passwrod must match'
        
        if User.objects.filter(email_address = postData['email_address'] ):
            errors['email_address'] = "Email already exists"

        return errors

class Messagemanager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['message']) < 10 :
            errors['message'] = 'message must be atleast 10 characters long'
        return errors

# class Commentmanager(models.Manager):
#     def basic_validator(self,postData):
#         errors = {}
#         if len(postData['comment']) < 10:
#             errors['comment'] = 'comment must be at least 10 characters'


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=60)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Usemanager()

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    objects = Messagemanager()

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
