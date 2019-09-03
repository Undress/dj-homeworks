from django.shortcuts import render
from phones.models import Phone
from django.http import HttpRequest

def show_catalog(request):

    template = 'catalog.html'
    context = {}
    context['data'] = []
    sort_by = request.GET.get('sort')

    phones = Phone.objects.all()

    if sort_by == 'name':
    	phones = Phone.objects.all().order_by('name')
    elif sort_by == 'price_low':
    	phones = Phone.objects.all().order_by('price')
    elif sort_by == 'price_high':
    	phones = Phone.objects.all().order_by('-price')


    for phone in phones:

    	context['data'].append({'name': phone.name, 'price': phone.price, 'image': phone.image, 
    		'release_date': phone.release_date, 'lte_exists': phone.lte_exists, 'slug': phone.slug})

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}

    phone = Phone.objects.filter(slug=slug).get()

    context['data'] = {'name': phone.name, 'price': phone.price, 'image': phone.image, 
    		'release_date': phone.release_date, 'lte_exists': phone.lte_exists}

    return render(request, template, context)
