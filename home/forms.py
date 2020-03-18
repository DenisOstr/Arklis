from django import forms

class ContactForm(forms.Form):
	fullName = forms.CharField(widget = forms.TextInput)
	email = forms.EmailField(widget = forms.TextInput)
	subject = forms.CharField(widget = forms.TextInput)
	description = forms.CharField(widget = forms.Textarea)