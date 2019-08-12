import datetime

from django.shortcuts import render
from books.models import Book
from django.core.exceptions import ObjectDoesNotExist


def books_view(request, date=None):

	template = 'books/books_list.html'
	context = {'data':[]}
	books_all = Book.objects.all().order_by('pub_date')


	if date:
		pub_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
		books = books_all.filter(pub_date=pub_date)

		try:
			books_before = books_all.filter(pub_date__lt=pub_date).reverse()[:1].get()
			context['prev_date'] = str(books_before.pub_date)
		except ObjectDoesNotExist:
			books_before = ''
		try:
			books_after = books_all.filter(pub_date__gt=pub_date)[:1].get()
			context['next_date'] = str(books_after.pub_date)
		except ObjectDoesNotExist:
			books_after = ''

		for book in books:
			context['data'].append({'name': book.name, 'author': book.author, 'pub_date': str(book.pub_date)})
		

	else:		
		for book in books_all:
			context['data'].append({'name': book.name, 'author': book.author, 'pub_date': str(book.pub_date)})

	print(context)
		
	return render(request, template, context)
