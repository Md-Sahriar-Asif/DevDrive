from django.contrib import admin
from .models import Blog, Category, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment)