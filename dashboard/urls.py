from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "dashboard"
urlpatterns = [

    path("password/", password_views,name='password'),
    
    path('users',users_views,name="users"), 
    path('updateuser/<int:id>',update_user,name="updateuser"),
    path('deleteuser/<int:id>',delete_user,name="deleteuser"), 
    
    
    
    path('pages',pages_views,name="pages"),
    path('page1',page1_views,name="page1"),   
    path('page2',page2_views,name="page2"),  
    path('page3',page3_views,name="page3"),  
    path('page4',page4_views,name="page4"), 
    
    path('edit_page1/<int:id>',edit_page1_views,name="edit_page1"),
    path('edit_page2/<int:id>',edit_page2_views,name="edit_page2"),    
    path('edit_page3/<int:id>',edit_page3_views,name="edit_page3"),    
    path('edit_page4/<int:id>',edit_page4_views,name="edit_page4"), 
     
    path('posts',posts_views,name="posts"),  
    path('adduser',add_user_views,name="adduser"),  
    path('addpost',add_post_views,name="addpost"),
    path('updatepost/<int:id>',update_post,name="updatepost"),
    path('deletepost/<int:id>',delete_post,name="deletepost"), 
 
 
 
    path('authors',authors_views,name="authors"), 
    path('addauthors',add_authors_views,name="addauthors"),  
    path('editauthors/<int:id>',edit_authors_views,name="editauthors"),
    path('deleteauthors/<int:id>',delete_authors_views,name="deleteauthors"),


    path('addtags',add_tags_views,name="addtags"),  
    path('edittags/<int:id>',edit_tags_views,name="edittags"),
    path('deletetags/<int:id>',delete_tags_views,name="deletetags"),

   
     
    path('images/<int:id>',images_views,name="images"),  
    path('submissions',submissions_views,name="submissions"),

    
    path('login/', LoginView.as_view(), name="custom_login"),
    path("logout/", LogoutView.as_view(), name="logout"),


    
]   

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
    