from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def validate_mail(value):
    if "@gmail.com" not in value:
        raise ValidationError("Please provide valid mail with '@gmail.com'")


class Student(models.Model):
    name = models.CharField(max_length=100)
    rool_number = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField(validators=[validate_mail])
    mobile = models.BigIntegerField(blank=True)
    branch = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
