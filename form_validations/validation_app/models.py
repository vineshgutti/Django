from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

def validate_mail(value):
    if '@gmail.com' not in value :
        raise ValidationError("Please provide valid mail with '@gmail.com'")
        

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    rool_number = models.IntegerField()
    age = models.IntegerField()
    email= models.EmailField(validators=[validate_mail])
    mobile = models.BigIntegerField() 
    branch = models.CharField(max_length=30)
    description = models.TextField(validators=[validators.MaxLengthValidator(10)],null=True,blank=True)
    
    def __str__(self):
        return self.name