from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=30,null=True)
    age = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=20,null=True)
    department = models.CharField(max_length=30,null=True)
    salary = models.IntegerField(null=True)



    class Meta:
        db_table = 'Info'

