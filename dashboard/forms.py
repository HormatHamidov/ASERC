from django import forms
from django.forms import ModelForm
from matplotlib import widgets

from post.models import Article_Author, Image, Page1, Page2, Page3, Page4, Tag, User,Article  
from django.contrib.auth.forms import UserCreationForm ,UserChangeForm ,PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User  
        fields = ('first_name','last_name','username', 'email') 
        
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'username':'Username',
            'email':'Email',
        }
        
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),

        }
  
     
     
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=User 
        fields = ('first_name','last_name','username', 'email')
        
        
        labels = {
            'first_name':'First Name',
            'last_name':'Last Name',
            'username':'Username',
            'email':'Email',
        }
        
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),

        }
         
         
         
         
         

        
      
      
      
class PostForm(ModelForm):
    class Meta:
        model = Article
        fields = ('category','article_author','title','text','tag','fileurl')

        labels = {
            'category':'Category',
            'title':'Title',
            'text':'Text',
            'tag':'Tags',
            'fileurl':'FileUrl'
        }
        
        widgets = {
            'category':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
            'fileurl':forms.FileInput(attrs={'class':'form-control'}),

        }
        
        


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['RightBarImage','LeftBarImage']
        
        labels = {
            'RightBarImage':'RightBarImage',
            'LeftBarImage':'LeftBarImage',
        }
        
        widgets = {
            'RightBarImage':forms.FileInput(attrs={'class':'form-control'}),
            'LeftBarImage':forms.FileInput(attrs={'class':'form-control'}),
        }
        
        
 
    
class Page1Form(forms.ModelForm):
    class Meta:
        model = Page1
        fields = ('pagename','title','text')
        
        labels = {
            'pagename':'Page name',
            'title':'Title',
            'text':'Text',
        }
        
        widgets = {
            'pagename':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
        }
        
        
class Page2Form(forms.ModelForm):
    class Meta:
        model = Page2
        fields = ('pagename','title','text')
        
        labels = {
            'pagename':'Page name',
            'title':'Title',
            'text':'Text',
        }
        
        widgets = {
            'pagename':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
        }
        
class Page3Form(forms.ModelForm):
    class Meta:
        model = Page3
        fields = ('pagename','title','text')
        
        labels = {
            'pagename':'Page name',
            'title':'Title',
            'text':'Text',
        }
        
        widgets = {
            'pagename':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
        }
        
class Page4Form(forms.ModelForm):
    class Meta:
        model = Page4
        fields = ('pagename','title','text')
        
        labels = {
            'pagename':'Page name',
            'title':'Title',
            'text':'Text',
        }
        
        widgets = {
            'pagename':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'form-control'}),
        }
        
        
        
class AuthorForms(forms.ModelForm):
    class Meta:
        model = Article_Author
        
        fields = ('name',)
        
        labels = {
            'name':'Name',
        }
        
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }

        
    
    
    
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        
        fields = ('text',)
        
        labels = {
            'text':'Text',
        }
        
        widgets = {
            'text':forms.TextInput(attrs={'class':'form-control'}),
        }
        

                