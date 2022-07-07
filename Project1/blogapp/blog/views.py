from operator import truediv
from tracemalloc import is_tracing
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category


# Create your views here.

def index(request):
    contex = {
        "blogs": Blog.objects.filter(is_home = True, is_active = True),
        "categories": Category.objects.all()
    }
    #render come from django.shortcuts import render and render returns an HttpResponse object with that rendered text.
    return render(request, "blog/index.html", contex) #search all app templates folders and find index.html then send it

def blogs(request):
    contex = {
        "blogs": Blog.objects.filter(is_active = True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", contex) #searching blogs.html inside of template/blog folders and then send it 

def blogs_details(request, slug):   
    blog = Blog.objects.get(slug = slug)
    return render(request, "blog/blog_details.html", {"blog":blog}) #searching blogs_detail.html inside of template/blog folders and then send it
    # third variable is sending variable to the html file for writing to the website

def blogs_by_category(request, slug):
    contex = {
        "blogs": Category.objects.get(slug = slug).blog_set.filter(is_active = True),
        #"blogs": Blog.objects.filter(is_active = True, category__slug = slug),
        "categories": Category.objects.all(),
        "selected_category": slug,
    }
    return render(request, "blog/blogs.html", contex)   
