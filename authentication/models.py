from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class answer(models.Model):
#     # fname=models.CharField(max_length=50)
#     # lname=models.CharField(max_length=50)
#     # email=models.EmailField(max_length=255)
    id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=50)
    answer1=models.IntegerField()
    answer2=models.IntegerField()
    answer3=models.IntegerField()
    answer4=models.IntegerField()
    answer5=models.IntegerField()
    answer6=models.IntegerField()
    answer7=models.IntegerField()
    answer8=models.IntegerField()
    answer9=models.IntegerField()
    answer10=models.IntegerField()
    date=models.DateTimeField()
    result=models.CharField(max_length=50)

class detail(models.Model):
    username=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    

class question(models.Model):
    questions=models.TextField()
    


