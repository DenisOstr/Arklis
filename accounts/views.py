from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import auth

from .forms import RegisterForm, LoginForm, UpdateForm
from .models import Account


def register(request):
	userActive = request.user.is_authenticated

	if userActive:
		raise Http404
	else:
		if request.method == 'POST':
			form = RegisterForm(request.POST)

			if form.is_valid():
				form.save()
				# firstName = request.POST.get('firstName')
				# lastName = request.POST.get('lastName')
				# username = request.POST.get('username')
				# email = request.POST.get('email')
				# password = request.POST.get('password')

				# data = Account(
				# 	firstName = firstName,
				# 	lastName = lastName,
				# 	username = username,
				# 	email = email,
				# 	password = password
				# )

				# data.save()
				return redirect('successRegister')

			context = {
				'form': form
			}

			return render(request, 'accounts/register.html', context)
		else:
			form = RegisterForm()

			context = {
				'form': form
			}

			return render(request, 'accounts/register.html', context)


def successRegister(request):
	userActive = request.user.is_authenticated

	if userActive:
		raise Http404
	else:
		return render(request, 'accounts/register_success.html')


def login(request):
	userActive = request.user.is_authenticated

	if userActive:
		raise Http404
	else:
		if request.method == 'POST':
			form = LoginForm(request.POST)

			print('Method DONE!!!')

			context = {
				'form': form
			}

			if form.is_valid():
				print('Form valid DONE!!!')

				username = request.POST.get('username')
				password = request.POST.get('password')

				print(type(username))
				print(type(password))

				user = auth.authenticate(request, username = username, password = password)

				if user is not None:
					auth.login(request, user)
					print('Auth DONE!!!')
					return redirect('/')
				else:
					print('Auth Error!!!')
					return redirect('register')

				print('Login DONE!!!')

			form = LoginForm()
			return render(request, 'accounts/login.html', context)
		else:
			print('Get Login DONE!!!')
			form = LoginForm()

			context = {
				'form': form
			}

			return render(request, 'accounts/login.html', context)


def logout(request):
	auth.logout(request)

	return redirect('login')


def profile(request):
	userActive = request.user.is_authenticated

	if not userActive:
		raise Http404
	else:
		return render(request, 'accounts/profile.html')


def updateUserInfo(request):
	userActive = request.user.is_authenticated

	if not userActive:
		raise Http404
	else:
		if request.method == 'POST':
			form = UpdateForm(request.POST)

			context = {
				'form': form
			}

			if form.is_valid():
				firstName = request.POST.get('firstName')
				lastName = request.POST.get('lastName')
				email = request.POST.get('email')

				obj = Account.objects.filter(pk = request.user.pk)
				obj.update(firstName = firstName, lastName = lastName, email = email)

				return redirect('profile')

			form = UpdateForm()
			return render(request, 'accounts/update_user_info.html', context)
		else:
			form = UpdateForm()

			context = {
				'form': form
			}

			return render(request, 'accounts/update_user_info.html', context)