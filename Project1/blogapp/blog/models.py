from pickle import TRUE
from sre_parse import CATEGORIES
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField   

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 151)
    slug = models.SlugField(null = False, blank = True, unique = True, db_index = True, editable = False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save( *args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = "blogs")
    decription = RichTextField()
    is_active = models.BooleanField(default = False) 
    is_home = models.BooleanField(default = False)
    slug = models.SlugField(null = False, blank = True, unique = True, db_index = True, editable = False)
    
    #we give default = 1 for exist entrys also we can solve it this problem with otheer solutions
    #category = models.ForeignKey(Category, default = 1, on_delete = models.CASCADE) #ForeignKey = if u use to another tablo id this is ForeignKey (in there we want to use category's id)
    categories = models.ManyToManyField(Category, blank = True)


    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):    
        self.slug = slugify(self.title)
        super().save( *args, **kwargs)



    