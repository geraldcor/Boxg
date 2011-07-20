import random
import datetime
from math import fabs
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.core.mail import EmailMessage
from boxg.home.models import Artists, ArtistImages, Exhibition, Hours, SubmissionPDF
from boxg.home.forms import ContactForm

def index(request):
	# Get the pool of objects for our random list
	#picture_pool = ArtistImages.objects.all().order_by('?')[:100]
	#pictures = ArtistImages.objects.all().order_by('?')[:100]
	exhibit = Exhibition.objects.filter(begin_date__lte=datetime.date.today()).order_by('-begin_date')[:1]
	# Randomly select objects from the pool
	#pictures = random.sample(picture_pool, 8)
	return render_to_response('index.html', {'exhibit':exhibit}, context_instance=RequestContext(request))

def past(request, exhibit_id=None):
	#archives = {datetime.date.today().year:['' for x in range(12)]}
	months = ['dec', 'nov', 'oct', 'sep', 'aug', 'jul', 'jun', 'may', 'apr', 'mar', 'feb', 'jan']
	arch = Exhibition.objects.values('begin_date', 'id', 'name').order_by('-begin_date')
	archives = {datetime.date.today().year:[[x] for x in months]}
	for a in arch:
		if a['begin_date'].year == datetime.date.today().year:
			archives[datetime.date.today().year][int(fabs(a['begin_date'].month-12))].append([a['id'], a['name']])
		else:
			try:
				archives[a['begin_date'].year][a['begin_date'].month-int(fabs(12))].append([a['id'], a['name']])
			except:
				archives[a['begin_date'].year] = [[x] for x in months]
				archives[a['begin_date'].year][a['begin_date'].month-int(fabs(12))].append([a['id'], a['name']])
	if exhibit_id:
		exhibit = Exhibition.objects.filter(id__exact=exhibit_id)
	else:
		exhibit = Exhibition.objects.order_by('-begin_date')[:1]
	return render_to_response('past.html', {'exhibit':exhibit, 'archives':archives}, context_instance=RequestContext(request))
	
def artists(request):
	artists = Artists.objects.filter(hide=False).order_by('name')
	return render_to_response('all_artists.html', {'artists':artists}, context_instance=RequestContext(request))
	
def artist(request, art_id):
	artist = Artists.objects.get(id=art_id)
	return render_to_response('artist.html', {'artist':artist}, context_instance=RequestContext(request))
	
def contact(request):
	if request.method == 'POST':
		recipients = ['michelle@boxgallerysf.com']
		#Change ['gregcorey@gmail.com'] to ['email@example.com', 'another@example.com', etc] Can be as many as you like
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			name = form.cleaned_data['name']
			sender = form.cleaned_data['sender']
			message = 'This email is coming from %s <%s>.\n\n' % (name, sender)
			message += form.cleaned_data['message']
			email = EmailMessage(subject, message, to = recipients, headers = {'Reply-To': sender})
			if email.send():
				return HttpResponse("success")
			else:
				return HttpResponse("There was an error sending your email")
	else:
		form = ContactForm()
		hours = Hours.objects.get(id=1)
		submission = SubmissionPDF.objects.get(id=1)
	return render_to_response('contact.html', {'form':form, 
'hours':hours, 'submission':submission}, context_instance=RequestContext(request))
