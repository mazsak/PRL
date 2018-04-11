from django.shortcuts import render

from django.http import HttpResponse
from .models import Zawodnik

def index(request):
	return HttpResponse("Piłkarskie rozgrywki ligowe")

def detail(request, zawodnik_id):
	return HttpResponse("You're looking at question %s." % zawodnik_id)

def results(request, zawodnik_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % zawodnik_id)

def vote(request, zawodnik_id):
	return HttpResponse("You're voting on question %s." % zawodnik_id)

#def index(request):
	#latest_zawodnik_list = Zawodnik.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.zawodnik_text for q in latest_zawodnik_list])
	#return HttpResponse(output)





