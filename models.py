from django.db import models

# Create your models here.
import datetime

from django.utils import timezone

# Create your models here.
class Questions(models.Model):
    question_text=models.CharField(max_length=200)
    publish_date=models.DateTimeField("date pusblished")

    #Gives string representation of the object.
    # def __str__(self):
    #     return self.question_text
  

class Choice(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.PositiveIntegerField(default=0)

    # def __str__(self):
    #     return self.choice_text