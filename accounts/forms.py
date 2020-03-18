from django import forms
from django.contrib import auth
# from django.contrib.auth import get_user_model
from django.db.models import Q

from .validation import *

from .models import Account

# User = get_user_model()

class RegisterForm(forms.ModelForm):
	firstName = forms.CharField(widget = forms.TextInput)
	lastName = forms.CharField(widget = forms.TextInput)
	username = forms.CharField(widget = forms.TextInput)
	email = forms.EmailField(widget = forms.EmailInput)
	emailConfirm = forms.EmailField(widget = forms.EmailInput)
	password = forms.CharField(widget = forms.PasswordInput)
	passwordConfirm = forms.CharField(widget = forms.PasswordInput)


	class Meta:
		model = Account
		fields = [
			'firstName',
			'lastName',
			'username',
			'email',
			'emailConfirm',
			'password',
			'passwordConfirm',
		]


	def clean_username(self):
		username = self.cleaned_data.get('username')

		us = Account.objects.filter(username = username)

		if us.exists():
			raise forms.ValidationError('User name is taken')
		return username


	def clean_emailConfirm(self):
		email = self.cleaned_data.get('email')
		emailConfirm = self.cleaned_data.get('emailConfirm')

		qs = Account.objects.filter(email = email)

		if qs.exists():
			raise forms.ValidationError('This email is already registred!')
		if email and emailConfirm and email != emailConfirm:
			raise forms.ValidationError('Email does not matched!')
		return emailConfirm


	def clean_passwordConfirm(self):
		password = self.cleaned_data.get('password')
		passwordConfirm = self.cleaned_data.get('passwordConfirm')

		if password and passwordConfirm and password != passwordConfirm:
			raise forms.ValidationError('Passwords does not matched!')
		return passwordConfirm


	def save(self, commit = True):
		user = super(RegisterForm, self).save(commit = False)
		user.set_password(self.cleaned_data['password'])

		if commit:
			user.save()

		return user


class LoginForm(forms.Form):
	username = forms.CharField(widget = forms.TextInput)
	password = forms.CharField(widget = forms.PasswordInput)


	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		us = Account.objects.filter(username = username)

		# if is_empty(us):
		# 	raise forms.ValidationError('Username does not exists!')
		# return username

		if username and password:
			user = auth.authenticate(username = username, password = password)

			if not user:
				raise forms.ValidationError('User does not exists!')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password!')

		# return super(LoginForm, self).clean(*args, **kwargs)


class UpdateForm(forms.ModelForm):
	firstName = forms.CharField(widget = forms.TextInput)
	lastName = forms.CharField(widget = forms.TextInput)
	email = forms.EmailField(widget = forms.EmailInput)


	class Meta:
		model = Account
		fields = [
			'firstName',
			'lastName',
			'email',
		]


	def clean(self):
		firstName = self.cleaned_data.get('firstName')
		lastName = self.cleaned_data.get('lastName')
		email = self.cleaned_data.get('email')

		if not firstName:
			raise forms.ValidationError('Please enter your name')
		if not lastName:
			raise forms.ValidationError('Please enter your surname')
		if not email:
			raise forms.ValidationError('Please enter your email')