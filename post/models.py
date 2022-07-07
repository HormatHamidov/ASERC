from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.




class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    
    
    
class Page1(models.Model):
    pagename = models.CharField(default="",max_length=50,verbose_name="Page name")
    title = models.CharField(max_length=50)
    text = RichTextField()
    
    def __str__(self):
        return self.pagename
  
    
class Page2(models.Model):
    pagename = models.CharField(default="",max_length=50,verbose_name="Page name")
    title = models.CharField(max_length=50)
    text = RichTextField()
    
    def __str__(self):
        return self.pagename
    
    
    
class Page3(models.Model):
    pagename = models.CharField(default="",max_length=50,verbose_name="Page name")
    title = models.CharField(max_length=50)
    text = RichTextField()
    
    def __str__(self):
        return self.pagename

    
    
class Page4(models.Model):
    pagename = models.CharField(default="",max_length=50,verbose_name="Page name")
    title = models.CharField(max_length=50)
    text = RichTextField()
    
    def __str__(self):
        return self.pagename
    
    
    

class Image(models.Model):
    LeftBarImage = models.ImageField(upload_to='media/',verbose_name="LeftBar Image",blank=True, null=True,height_field=None, width_field=None)
    RightBarImage = models.ImageField(upload_to='media/',verbose_name="RightBar Image",blank=True, null=True,height_field=None, width_field=None)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.RightBarImage)
    
    def __str__(self):
        return str(self.LeftBarImage)
    
  
class Submission(models.Model):
    articletitle = models.CharField(max_length=50,validators=[MinLengthValidator(3)])
    author_name = models.CharField(max_length=40,validators=[MinLengthValidator(3)])
    affiliation_name = models.CharField(max_length=30,default='',verbose_name="Author's primary affiliation")
    author_email = models.EmailField(blank=True)
    country = models.CharField(max_length=40,default='')
    firstname = models.CharField(max_length=30,validators=[MinLengthValidator(3)], blank=True,verbose_name='Name')
    lastname = models.CharField(max_length=30,validators=[MinLengthValidator(3)], blank=True , verbose_name='Surname')
    email = models.EmailField(blank=True)
    keywords =models.CharField(max_length=70)
    abstracted = models.TextField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.articletitle
    
  

class Tag(models.Model):
    text = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text


class Article_Author(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    category = models.CharField(max_length=30)
    article_author = models.ManyToManyField(Article_Author)
    title = models.CharField(max_length=50)
    text = RichTextField()
    fileurl = models.ImageField(upload_to='media/ArticleImages',blank=True, null=True)
    status = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag) 
    
    def __str__(self):
        return self.category
      
    
class ArticleTag(models.Model):
    articleid = models.ForeignKey(Article, on_delete=models.CASCADE)
    tagid = models.ManyToManyField(Tag)
    status = models.BooleanField(default=False)

