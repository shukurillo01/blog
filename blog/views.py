from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from datetime import datetime
from django.contrib.auth.models import User
from .forms import BlogForm,MyUserCreationFrom

def index(request):
    maqolalar = Blog.objects.all().order_by('-id')
    return render(request,"index.html",  {'blogs':maqolalar})

def blog_detail(request,blog_id):
    blog=Blog.objects.get(id=blog_id)
    return render (request,"blog_detail.html",{"blog":blog})

def blog_yarat(request):
    form=BlogForm
    if request.method == 'POST':
        form=BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        return render(request,"blog_yarat.html",{'form':form})
    return render(request,"blog_yarat.html",{'form':form})
   
def blog_taxrirlash(request, blog_id):
    blog=Blog.objects.get(id=blog_id)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form=BlogForm(instance=blog, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        return render(request,"blog_taxrirlash.html",{'form':form})
    return render(request,"blog_taxrirlash.html",{'form':form})

def blog_ochrish(request,blog_id):


    blog= Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect("index")
    return render(request, 'blog_ochirish.html',{'blog':blog})

def signub(request):
    form = MyUserCreationFrom
    if request.method== 'POST':
        form = MyUserCreationFrom(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
             return render (request,'registration/singup.html',{'form':form})

    return render (request,'registration/singup.html',{'form':form})
