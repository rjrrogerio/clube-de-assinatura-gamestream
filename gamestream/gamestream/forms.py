from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	
	username = forms.CharField(
        label ='Nome de usuário',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),)

	email = forms.EmailField(
		required=True,
		label ='Email',
        widget=forms.TextInput(attrs={'placeholder':'Email','class': 'form-control mb-3'}),)

	password1 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
    label='Insira sua senha')

	password2 = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
    label='Repita sua senha')			

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user