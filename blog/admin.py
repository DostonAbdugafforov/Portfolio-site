from django.contrib import admin
from .models import Blog, Comment, BlogCategory, AboutMe, Contact


admin.site.register([Blog, Comment, BlogCategory, AboutMe, Contact])
