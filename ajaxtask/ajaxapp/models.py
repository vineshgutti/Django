from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    mobile = models.CharField(max_length=10)
    area = models.CharField(max_length=50)
    days = models.PositiveIntegerField()
    salary = models.FloatField(default=300)

    def __str__(self):
        return self.name
