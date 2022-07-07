from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home","slug","selected_categories",) #list_display is feaute from django admin / display this features
    list_editable = ("is_active","is_home") #list_editable is feaute from django admin / add editable box 
    search_fields = ("title","decription") #search_field is feaute from django admin / add search field
    readonly_fields = ("slug",) #readonly_fields is feaute from django admin / you can just read can not change 
    list_filter = ("is_home","is_active")

    def selected_categories(self, obj):
        html = ""
        
        for category in obj.categories.all():
            html += category.name + " "

        return html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug")
    readonly_fields = ("slug",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)