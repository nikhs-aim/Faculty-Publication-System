
from django.contrib.auth.forms import UserCreationForm
from .models import Faculty
from django import forms
from .models import Post,Event


class RegistrationForm(UserCreationForm):
    name=forms.CharField(max_length=100,label='Full Name')
    username=forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    department_name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    password1=forms.CharField(widget=forms.PasswordInput(),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')

    class Meta(UserCreationForm.Meta):
        model = Faculty
        fields = ('name','username', 'age', 'email', 'role', 'gender','department_name','phone_number','password1','password2')

    def clean_username(self):
        username= self.cleaned_data.get('username')
        if Faculty.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_snap', 'post_details', 'post_category']


