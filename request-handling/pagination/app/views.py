import csv
import itertools
import urllib

from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpRequest
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

	context = {}
	context['bus_stations'] = []
	current_page_num = 1


	if request.GET.get('page'):
		current_page_num = int(request.GET.get('page'))

	
	context['current_page'] = current_page_num	

	with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as csvfile:

		file_content = list(csv.DictReader(csvfile))
		file_length = len(file_content)

		paginator = Paginator(file_content, 10)

		page = paginator.get_page(current_page_num)

		for row in page.object_list:
			context['bus_stations'].append({'Name': row['Name'], 'Street' : row['Street'], 'District' : row['District']})


	if page.has_next():
		context['next_page_url'] = reverse(bus_stations) + '?' + urllib.parse.urlencode({'page' : page.next_page_number()})
	else: 
		context['next_page_url'] = None

	if page.has_previous():
		context['prev_page_url'] = reverse(bus_stations) + '?' + urllib.parse.urlencode({'page' : page.previous_page_number()})
	else:
		context['prev_page_url'] = None 


	return render_to_response('index.html', context = context)


