from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Faculty
from django import forms
from .models import Post


class RegistrationForm(UserCreationForm):
    username=forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    department_name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password1=forms.CharField(widget=forms.PasswordInput(),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')

    class Meta(UserCreationForm.Meta):
        model = Faculty
        fields = ('username', 'age', 'email', 'role', 'gender','department_name','phone_number','password1','password2')





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_snap', 'post_details', 'post_category']
