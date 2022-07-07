from django.contrib import admin
from post.models import User
from django.contrib.auth.admin import UserAdmin
from .models import (Article, 
                     Article_Author, 
                     Image, 
                     Page1, 
                     Page2, 
                     Page3, 
                     Page4,
                     Submission,
                     Tag,
                     ArticleTag
                     )

# Register your models here.

class adminPage1(admin.ModelAdmin):
    list_display = ["pagename","id"]
    list_display_links = ["pagename"]
    list_filter = ["id"]
    search_fields = ["pagename"]
    
    class Meta:
        model = Page1

admin.site.register(Page1,adminPage1)


class adminPage2(admin.ModelAdmin):
    list_display = ["pagename","id"]
    list_display_links = ["pagename"]
    list_filter = ["id"]
    search_fields = ["pagename"]
    
    class Meta:
        model = Page2

admin.site.register(Page2,adminPage2)



class adminPage3(admin.ModelAdmin):
    list_display = ["pagename","id"]
    list_display_links = ["pagename"]
    list_filter = ["id"]
    search_fields = ["pagename"]
    
    class Meta:
        model = Page3

admin.site.register(Page3,adminPage3)



class adminPage4(admin.ModelAdmin):
    list_display = ["pagename","id"]
    list_display_links = ["pagename"]
    list_filter = ["id"]
    search_fields = ["pagename"]
    
    class Meta:
        model = Page4

admin.site.register(Page4,adminPage4)



class adminSubmission(admin.ModelAdmin):
    list_display = ["articletitle","id" , "author_name"]
    list_display_links = ["articletitle" , "author_name"]
    list_filter = ["articletitle"]
    search_fields = ["articletitle"]
    
    class Meta:
        model = Submission

admin.site.register(Submission,adminSubmission)


class adminTag(admin.ModelAdmin):
    list_display = ["text","id"]
    list_display_links = ["text"]
    list_filter = ["text"]
    search_fields = ["text"]
    
    class Meta:
        model = Tag

admin.site.register(Tag,adminTag)


class adminArticleTag(admin.ModelAdmin):
    list_display = ["id"]
    list_display_links = ["id"]
    list_filter = ["id"]
    search_fields = ["id"]
    
    class Meta:
        model = ArticleTag

admin.site.register(ArticleTag,adminArticleTag)






# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'classes': ('wide',),
                'fields':  ('status', )
            }
        ),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2')
            }
        ),
    )
    


class adminArticle(admin.ModelAdmin):
    list_display = ["category","title","id"]
    list_display_links = ["category"]
    list_filter = ["category"]
    search_fields = ["category"]
    
    class Meta:
        model = Article

admin.site.register(Article,adminArticle)



class adminArticleAuthor(admin.ModelAdmin):
    list_display = ["name","id"]
    list_display_links = ["name"]
    list_filter = ["name"]
    search_fields = ["name"]
    
    class Meta:
        model = Article_Author

admin.site.register(Article_Author,adminArticleAuthor)



class adminImage(admin.ModelAdmin):
    list_display = ["id"]
    list_display_links = ["id"]
    list_filter = ["id"]
    search_fields = ["id"]
    
    class Meta:
        model = Image

admin.site.register(Image,adminImage)