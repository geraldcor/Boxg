from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label="Your name",max_length=100)
	sender = forms.EmailField(label="Your email")
	subject = forms.CharField(label="Subject",max_length=100)
	message = forms.CharField(label="Message",widget=forms.Textarea)
