from django.shortcuts import render
from post.models import Article, Image,ArticleTag, Page1, Page2, Page3, Page4

from post.forms import SubmissionForm
from django.http import HttpResponseRedirect


def submission_views(request):
    submitted = False
    if request.method =="POST":
      form = SubmissionForm(request.POST)
      if form.is_valid():
        form.save()
        return HttpResponseRedirect('/submission?submitted=True')
    else:
      form = SubmissionForm
      if 'submitted' in request.GET:
        submitted = True
        
    my_images = Image.objects.all()  
    context={
       
      'my_images':my_images,
      'form':form,
      'submitted':submitted
    
    } 
    return render(request,"submission.html",context)


def home_views(request):
    my_images = Image.objects.all()
    my_pages1 = Page1.objects.all() 

    context={
       
      'my_images':my_images,
      'my_pages1':my_pages1,
    
    } 
    return render(request,"index.html",context)

def editorial_views(request):
    my_images = Image.objects.all()
    my_pages2 = Page2.objects.all()

    
    context={
       
      'my_images':my_images,
      'my_pages2':my_pages2,  
    } 
    return render(request,"editorial.html",context)

def guideline_views(request):
    my_images = Image.objects.all() 
    my_pages3 = Page3.objects.all() 

    context={
       
      'my_images':my_images,
      'my_pages3':my_pages3,  
    
    } 
    return render(request,"guideline.html",context)

def abstracted_views(request):
    my_images = Image.objects.all()  
    my_pages4 = Page4.objects.all()  

    context={
       
      'my_images':my_images,
      'my_pages4':my_pages4,  

    
    } 
    return render(request,"abstracted.html",context)



def category_views(request):

    my_data = Article.objects.all()
    my_images = Image.objects.all() 

    context={
       
      'my_data':my_data,
      'my_images':my_images,
    
    } 

    return render(request, "category.html", context)
  
  
  
  
def categoryid_views(request,name):

    my_data = Article.objects.filter(category = name)
    my_images = Image.objects.all()

    context={
       
      'my_data':my_data,
      'my_images':my_images,
    
    } 

    return render(request, "category.html", context)



def categorydetails_views(request):

    my_data = Article.objects.all()
    my_tag = ArticleTag.objects.all() 
    my_images = Image.objects.all()  

    context={
       
      'my_data':my_data,
      'my_tag':my_tag,
      'my_images':my_images
    
    } 

    return render(request, "categorydetails.html", context)



def categorydetailid_views(request,id):

    my_data = Article.objects.get(id=id) 
    my_tag = ArticleTag.objects.filter(articleid_id=id).order_by('articleid__category')
    my_images = Image.objects.all() 

    context={
       
      'article':my_data,
      'my_tag':my_tag,
      'my_images':my_images
    
    } 

    return render(request, "categorydetails.html", context)
  
  

