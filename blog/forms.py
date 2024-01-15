from django.forms import ModelForm
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['sarlovha', 'tanasi', 'vaqt', 'rasm']




class  MyUserCreationFrom(UserCreationForm):
    class Meta:
       model = User
       fields = ['username','email','first_name','password1','password2']