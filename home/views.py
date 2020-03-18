from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from .forms import ContactForm

def index(request):
	# if request.method == 'POST':
	form = ContactForm(request.POST)

	if form.is_valid():
		sender_name = form.cleaned_data['fullName']
		sender_email = form.cleaned_data['email']
		sender_subject = form.cleaned_data['subject']

		message = '{0} has sent you a new message:\n\n{1}'.format(sender_name, form.cleaned_data['description'])
		send_mail(sender_subject, message, sender_email, ['denisostrovskis1@gmail.com'])

		return redirect('/')
		# return HttpResponse('Thanks for contacting us!')
	else:
		form = ContactForm()

	context = {
		'form': form
	}

	return render(request, 'home/index.html', context)