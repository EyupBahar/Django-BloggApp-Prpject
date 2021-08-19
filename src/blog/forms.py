from django import forms
from .models import Post, Comment, Comment


class PostForm(models.Model):
    class Meta:
        model = Post
        fields = (' ')