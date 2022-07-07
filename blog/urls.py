"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from post.views import *
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_views,name="index"),
    path('editorial',editorial_views,name="editorial"),
    path('guideline',guideline_views,name="guideline"),
    path('abstracted',abstracted_views,name="abstracted"),
    path('submission',submission_views,name="submission"),
    path('category',category_views,name="category"),
    path('category/<str:name>/',categoryid_views,name="categoryid"),
    path('categorydetails',categorydetails_views,name="categorydetails"), 
    path('categorydetails/<int:id>/',categorydetailid_views,name="categorydetailid"), 
    
    path('dashboard/', include('dashboard.urls')),

 
  
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

