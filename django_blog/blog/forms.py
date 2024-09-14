from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
# blog/forms.py

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Fields to include in the form
# blog/forms.py

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
        }
from django import forms
from django.utils.safestring import mark_safe
from .models import Post
from taggit.models import Tag

class TagWidget(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Enter tags separated by commas'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

    def render(self, name, value, attrs=None, renderer=None):
        # If value is a list of tags, join them with commas for display
        if isinstance(value, list):
            value = ', '.join(value)
        return super().render(name, value, attrs, renderer)

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, widget=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        # Save instance first
        post = super(PostForm, self).save(commit=commit)

        # Process and set tags
        tags = self.cleaned_data['tags']
        if tags:
            # Clear existing tags and apply new ones
            post.tags.clear()
            post.tags.add(*[tag.strip() for tag in tags.split(',') if tag.strip()])
        
        if commit:
            post.save()
        return post
