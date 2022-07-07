from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from post.models import *


def password_views(request):
    return render(request,'registration/password.html')    
    
    
@login_required(login_url='/dashboard/login/')
# Create your views here.
def users_views(request):
    my_user = User.objects.all()

    context = {

        'my_user': my_user,

    }
    return render(request, 'dashboard/users.html', context)


@login_required(login_url='/dashboard/login/')
def add_user_views(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        form.save()

        return redirect("dashboard:users")
    return render(request, "dashboard/adduser.html", {"form": form})


@login_required(login_url='/dashboard/login/')
def update_user(request, id):

    deneme = get_object_or_404(User, id=id)
    form = CustomUserChangeForm(
        request.POST or None, request.FILES or None, instance=deneme)
    if form.is_valid():

        form.save()

        return redirect("dashboard:users")

    return render(request, "dashboard/update_user.html", {"form": form})


def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('dashboard:users')


@login_required(login_url='/dashboard/login/')
def pages_views(request):
    return render(request, 'dashboard/pages.html')


@login_required(login_url='/dashboard/login/')
def page1_views(request):
    my_page = Page1.objects.all()

    context = {

        'my_page': my_page,

    }
    return render(request, 'dashboard/page1.html', context)


def edit_page1_views(request, id):
    instance = Page1.objects.get(id=id)
    form = Page1Form(instance=instance)

    if request.method == 'POST':

        form = Page1Form(request.POST or None,
                         request.FILES or None, instance=instance)
        if form.is_valid():

            form.save()

            return redirect("dashboard:pages")

    context = {
        'form': form,
    }
    return render(request, "dashboard/edit_page1.html", context)


def edit_page2_views(request, id):
    instance = Page2.objects.get(id=id)
    form = Page2Form(instance=instance)

    if request.method == 'POST':

        form = Page2Form(request.POST or None,
                         request.FILES or None, instance=instance)
        if form.is_valid():

            form.save()

            return redirect("dashboard:pages")

    context = {
        'form': form,
    }
    return render(request, "dashboard/edit_page2.html", context)


def edit_page3_views(request, id):
    instance = Page3.objects.get(id=id)
    form = Page3Form(instance=instance)

    if request.method == 'POST':

        form = Page3Form(request.POST or None,
                         request.FILES or None, instance=instance)
        if form.is_valid():

            form.save()

            return redirect("dashboard:pages")

    context = {
        'form': form,
    }
    return render(request, "dashboard/edit_page3.html", context)


def edit_page4_views(request, id):
    instance = Page4.objects.get(id=id)
    form = Page4Form(instance=instance)

    if request.method == 'POST':

        form = Page4Form(request.POST or None,
                         request.FILES or None, instance=instance)
        if form.is_valid():

            form.save()

            return redirect("dashboard:pages")

    context = {
        'form': form,
    }
    return render(request, "dashboard/edit_page4.html", context)


@login_required(login_url='/dashboard/login/')
def page2_views(request):
    my_page = Page2.objects.all()

    context = {

        'my_page': my_page,

    }
    return render(request, 'dashboard/page2.html', context)


@login_required(login_url='/dashboard/login/')
def page3_views(request):
    my_page = Page3.objects.all()

    context = {

        'my_page': my_page,

    }
    return render(request, 'dashboard/page3.html', context)


@login_required(login_url='/dashboard/login/')
def page4_views(request):
    my_page = Page4.objects.all()

    context = {

        'my_page': my_page,

    }
    return render(request, 'dashboard/page4.html', context)


@login_required(login_url='/dashboard/login/')
def submissions_views(request):
    my_sub = Submission.objects.all()

    context = {

        'my_sub': my_sub,

    }

    return render(request, 'dashboard/submissions.html', context)


@login_required(login_url='/dashboard/login/')
def posts_views(request):
    my_post = Article.objects.all()

    context = {

        'my_post': my_post,

    }
    return render(request, 'dashboard/posts.html', context)


@login_required(login_url='/dashboard/login/')
def add_post_views(request):
    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save()

        article.save()

        return redirect("dashboard:posts")
    return render(request, "dashboard/addpost.html", {"form": form})


@login_required(login_url='/dashboard/login/')
def update_post(request, id):

    article = get_object_or_404(Article, id=id)
    form = PostForm(request.POST or None,
                    request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save()

        article.save()

        return redirect("dashboard:posts")

    return render(request, "dashboard/update_posts.html", {"form": form})


def delete_post(request, id):
    post = get_object_or_404(Article, id=id)
    post.delete()
    return redirect('dashboard:posts')


@login_required(login_url='/dashboard/login/')
def images_views(request, id):
    instance = Image.objects.get(id=id)
    form = ImageForm(request.POST, request.FILES, instance=instance)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('dashboard:users')
    else:
        form = ImageForm(request.POST, request.FILES, instance=instance)
    return render(request, 'dashboard/images.html', {'form': form})


@login_required(login_url='/dashboard/login/')
def authors_views(request):
    my_post = Article_Author.objects.all()
    my_tags = Tag.objects.all()

    context = {
        'my_post': my_post,
        'my_tags': my_tags,

    }
    return render(request, "dashboard/authors.html", context)





def add_tags_views(request):
    form = TagForm()

    if request.method == 'POST':

        form = TagForm(request.POST or None,
                         request.FILES or None)
        if form.is_valid():

            form.save()

            return redirect("dashboard:authors")

    context = {
        'form': form,
    }
    return render(request, "dashboard/add_tags.html",context)


def edit_tags_views(request, id):
    instance = Tag.objects.get(id=id)
    form = TagForm(instance=instance)

    if request.method == 'POST':

        form = TagForm(request.POST or None,
                         request.FILES or None, instance=instance)
        if form.is_valid():

            form.save()

            return redirect("dashboard:authors")

    context = {
        'form': form,
    }
    return render(request, "dashboard/edit_tags.html", context)


def delete_tags_views(request, id):
    post = get_object_or_404(Tag, id=id)
    post.delete()
    return redirect('dashboard:authors')


# **************
#  AUTHORS
# **************


def add_authors_views(request):
    form = AuthorForms()

    if request.method == 'POST':

        form = AuthorForms(request.POST or None,
                         request.FILES or None)
        if form.is_valid():

            form.save()

            return redirect("dashboard:authors")

    context = {
        'form': form,
    }
    return render(request, "dashboard/addauthors.html", context)




def edit_authors_views(request, id):
    instance = Article_Author.objects.get(id=id)
    form = AuthorForms(instance=instance)

    if request.method == 'POST':

        form = AuthorForms(request.POST or None,
                         request.FILES or None, instance=instance)
        if form.is_valid():

            form.save()

            return redirect("dashboard:authors")

    context = {
        'form': form,
    }
    return render(request, "dashboard/edit_authors.html", context)





def delete_authors_views(request, id):
    post = get_object_or_404(Article_Author, id=id)
    post.delete()
    return redirect('dashboard:authors')




    
    
