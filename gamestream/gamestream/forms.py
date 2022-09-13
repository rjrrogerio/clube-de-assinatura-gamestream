from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
<<<<<<< HEAD
	
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

=======
	email = forms.EmailField(required=True)
>>>>>>> 3680c1f86bdb4a5b37416fe6a0cd6dc2ec729eb9
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user