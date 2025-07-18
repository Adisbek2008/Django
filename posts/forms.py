from django import forms
from posts.models import Post

# Вариант №1
class PostForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(required=True, max_length=256)
    content = forms.CharField(required=True, max_length=456)

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title and title.lower() == 'python':
            raise forms.ValidationError("Title cannot be Python")
        
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title and content and title.lower() == content.lower():
            raise forms.ValidationError("Title and content cannot be same")
        return cleaned_data


# Вариант №2
class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']