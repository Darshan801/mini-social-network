from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['profile_image', 'profile_bio']  # fields user can edit
        widgets = {
            'profile_bio': forms.TextInput(attrs={
                'class': 'border p-2 rounded w-full',
                'placeholder': 'Write something...'
            })
        }
