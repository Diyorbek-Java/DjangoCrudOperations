from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    # firs_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    # last_name = forms.CharField(label="",max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Second Name'}))


    class Meta:
        model = User
        fields = ('username','first_name','last_name','email',"password1",'password2')
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
