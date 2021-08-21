from django.contrib import admin
from .models import  Post, Comment, Like, PostView, Category

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Like)
