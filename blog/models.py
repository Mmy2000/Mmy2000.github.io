from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify 



class Post(models.Model):
    auther = models.ForeignKey(User, related_name="post_auther",verbose_name=('auther'), on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name=('title'))
    tags = TaggableManager(("tags"))
    image = models.ImageField(("image"),upload_to='post/')
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    description = models.TextField(("description"),max_length=100000)
    category = models.ForeignKey('Category',related_name='post_category',verbose_name=('category'),on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
    



class Category(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
