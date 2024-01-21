from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

from django.forms.widgets import PasswordInput, TextInput

from django import forms

from .models import Task



# Register a user
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Login a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# - Create a Task
class CreateTaskForm(forms.ModelForm):

    class Meta:

        model = Task
        fields = ['title', 'content',]
        exclude = ['user',]


# - Update a User
class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:
        model = User
        fields = ['username', 'email',]
        exclude = ['password1', 'password2', ]



# - Update a profile picture
class UpdateProfileForm(forms.ModelForm):

    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:
        model = User
        fields = ['profile_pic',]





