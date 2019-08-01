import csv
import itertools
import urllib

from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpRequest



def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):

	context = {}
	context['bus_stations'] = []
	current_page_num = 1
	prev_page_num = None
	next_page_num = 2
	file_length = 0
	last_row = 0


	if request.GET.get('page'):
		current_page_num = int(request.GET.get('page'))
		next_page_num = current_page_num + 1
		prev_page_num = current_page_num - 1
	
	context['current_page'] = current_page_num	

	if prev_page_num == 0 or prev_page_num == None: 
		context['prev_page_url'] = None 
	else:
		context['prev_page_url'] = reverse(bus_stations) + '?' + urllib.parse.urlencode({'page' : prev_page_num})
	

	with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as csvfile:

		file_content = list(csv.DictReader(csvfile))
		file_length = len(file_content)

		for row in itertools.islice(file_content, (current_page_num - 1) * 10, (next_page_num - 1) * 10):
			context['bus_stations'].append({'Name': row['Name'], 'Street' : row['Street'], 'District' : row['District']})
			last_row = file_content.index(row)


	if last_row == file_length - 1:
		context['next_page_url'] = None
	else:
		context['next_page_url'] = reverse(bus_stations) + '?' + urllib.parse.urlencode({'page' : next_page_num})



	return render_to_response('index.html', context = context)


