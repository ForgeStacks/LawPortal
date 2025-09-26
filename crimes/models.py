from django.db import models

# Create your models here.

    
    
class User(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    age = models.IntegerField(blank= False)
    email = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=60, blank=False)
    is_authenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.email
