from django.contrib import admin
from .models import Author, Category, Course, Comment
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Comment)
