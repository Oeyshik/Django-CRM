from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=froms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = froms.CharField(label="", max_length="25", widget=froms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length="25", widget=froms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = username
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')