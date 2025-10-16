from django.contrib import admin
from .models import Home, CategoryHome, Blog, BlogCategory, Client, Contact
# Register your models here.

admin.site.register([Home, CategoryHome, BlogCategory, Blog, Client, Contact])
