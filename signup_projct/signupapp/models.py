from django.db import models

# Create your models here.
class Registration(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    re_password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.firstname
    