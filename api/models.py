from django.db import models

# Create your models here.
class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    # A date filed storing "2022-10-23 18:50:10 +0530"
    date = models.DateTimeField()
    # User 
    user = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    software = models.CharField(max_length=100)
    # int field seats
    seats = models.IntegerField()
    # amount double field
    amount = models.FloatField()

