from django.db import models

class data(models.Model):
    fullname=models.CharField(max_length=20,default="")
    mobile = models.CharField(max_length=10,default="")
    email=models.CharField(max_length=20,default="")
    address1=models.CharField(max_length=50,default="")
    address2=models.CharField(max_length=50,default="")
    landmark=models.CharField(max_length=20,default="")
    city=models.CharField(max_length=20,default="")
    state=models.CharField(max_length=20,default="")
    pincode = models.CharField(max_length=6,default="")



   