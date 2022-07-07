from django.urls import path 
from . import views

#http://127.0.0.1:8000/ => homepage
#http://127.0.0.1:8000/index => homepage
#http://127.0.0.1:8000/blogs => blog
#http://127.0.0.1:8000/blogs/3 => blog-detail

urlpatterns = [
    path("",views.index, name = "home"), # meaning of "" = http://127.0.0.1:8000/
    path("index",views.index), # meaining of index = http://127.0.0.1:8000/index
    path("blogs",views.blogs, name = "blogs"), # meaning of blogs = http://127.0.0.1:8000/blogs
    path("category/<slug:slug>", views.blogs_by_category, name = "blogs_by_category"),
    path("blogs/<slug:slug>",views.blogs_details, name = "blog_details"), #<int:id> waiting int value after blogs/ and assign it to the id variable for send to the method
]