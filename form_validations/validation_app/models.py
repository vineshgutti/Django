from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    rool_number = models.IntegerField()
    age = models.IntegerField()
    email= models.EmailField()
    mobile = models.BigIntegerField(blank=True) 
    branch = models.CharField(max_length=30)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name