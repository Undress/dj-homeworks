import csv
from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    context = {}
    context['data'] = []
    data_fields = []

    with open ('inflation_russia.csv', newline='') as csvfile:
    	reader = list(csv.reader(csvfile, delimiter=';'))
    	for row in reader:
    		if reader.index(row) == 0:
    			context['header'] = row
    		else:
    			for index, item in enumerate(row):
    				try:
    					if index == 0:
    						row[index] = item	
    					else:
    						row[index] = float(item)
    				except ValueError:
    					row[index] = item 
    			context['data'].append(row)
    			# context[row[0]] = row[1:]
    		
    print(context)
    return render(request, template_name,
                  context)