import datetime
from django.db import models
from django.contrib.auth.models import User


class About(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20,null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    headline = models.CharField(max_length=50 , blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True )
    email = models.EmailField( max_length=254, blank=True, null=True)



    def __str__(self):
        return str(self.user)