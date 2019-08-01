import datetime
import os

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.urls import reverse




def file_list(request, date=None):
    template_name = 'index.html'
    
#     # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
#     context = {
# '       files': [
#             {'name': 'file_name_1.txt',
#              'ctime': datetime.datetime(2018, 1, 1),
#              'mtime': datetime.datetime(2018, 1, 2)}
#         ],
#         'date': datetime.date(2018, 1, 1)  # Этот параметр необязательн
#     }
    context = {}

    dir_list = os.listdir(settings.FILES_PATH)

    context['files'] = []
    for file in dir_list:
        file_path = f'{settings.FILES_PATH}/{file}' 
        file_data = os.stat(file_path)
        file_ctime = datetime.datetime.fromtimestamp(file_data.st_ctime)
        file_mtime = datetime.datetime.fromtimestamp(file_data.st_mtime)

        context['files'].append({'name' : file, 'ctime' : file_ctime, 'mtime' : file_mtime})

    if date:
        context['date'] = date

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_path = f'{settings.FILES_PATH}/{name}'
    f = open(file_path, "r")
    content = f.read()
    
    return render(
        request,
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': content}
    )

