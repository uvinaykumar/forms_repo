from django.db import models

class formsmodel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    sal=models.IntegerField()
    loc=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    username=models.CharField(max_length=100, null=True)
    password=models.CharField(max_length=10, null=True)

