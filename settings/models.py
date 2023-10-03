import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from django.urls import reverse




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
    

class Resume(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    year = models.CharField(max_length=50 , blank=True, null=True)
    subject = models.CharField(max_length=100 , blank=True, null=True)
    university = models.CharField(max_length=100 , blank=True, null=True)
    description = models.TextField(max_length=100000)

    def __str__(self):
        return str(self.user)
    

class Services(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey('Category',related_name='service_category',on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)



    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.category)
        super(Services,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse("service:service_detail", kwargs={"slug": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=60)
    icons = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Info(models.Model):
    site_name = models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    phone = models.CharField( max_length=30 , null=True, blank=True)
    email = models.EmailField( max_length=254 , null=True, blank=True)
    address = models.CharField( max_length=50 , null=True, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True )
    fb_link = models.URLField( max_length=200)
    twitter_link = models.URLField( max_length=200)
    instagram_link = models.URLField( max_length=200)

    def __str__(self):
        return self.site_name