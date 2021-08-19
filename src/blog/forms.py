from django import forms
from .models import Post, Commen, Category

class PostForm(models.Model):
    status = forms.ChoiceField(choices=Post.OPTIONS)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Select")
         
    class Meta:
        model = Post
        fields = (
            'title',
            'image',
            'content',
            'category',
            'status',
            )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)