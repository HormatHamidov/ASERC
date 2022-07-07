from post.models import Page1, Page2, Page3, Page4,Article

def navbar(request):
    my_pages1 = Page1.objects.all() 
    my_pages2 = Page2.objects.all() 
    my_pages3 = Page3.objects.all() 
    my_pages4 = Page4.objects.all() 
    my_data = Article.objects.all().order_by('category')   

    
    return {'my_pages1':my_pages1,'my_pages2':my_pages2,'my_pages3':my_pages3,'my_pages4':my_pages4,'my_data':my_data}
    
    
    

