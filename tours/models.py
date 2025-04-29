from django.db import models
from multiselectfield import MultiSelectField

# Package Model
class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    package_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    package_destinations = models.TextField(max_length=500)
    package_days = models.IntegerField()
    package_price = models.IntegerField()
    def __str__(self):
        return self.package_name

# User Model
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=60)
    phno = models.CharField(max_length=12,unique=True)
    pswd = models.CharField(max_length=16)
    
    def __str__(self):
        return self.user_name

# Booking Model
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    package_name = models.CharField(max_length=100,unique=False)  # Ensure the related name is correct
    user_name= models.CharField(max_length=60,unique=False)
    phno = models.CharField(max_length=12,unique=False)
    status = models.CharField(max_length=15, default="Requested")
    date=models.CharField(max_length=12)
    persons=models.IntegerField()
    amt=models.IntegerField()
    payment_method=models.CharField(max_length=50,null=True)
    payment_address=models.CharField(max_length=250)

    def __str__(self):
        return f"Booking {self.booking_id} - {self.package_name}"


    