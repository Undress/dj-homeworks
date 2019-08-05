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

    if date:
        context['date'] = datetime.datetime.strptime(date, '%Y-%m-%d')
        print(context['date'])

    for file in dir_list:
        file_path = f'{settings.FILES_PATH}/{file}' 
        file_data = os.stat(file_path)
        file_ctime = datetime.datetime.fromtimestamp(file_data.st_ctime)
        file_mtime = datetime.datetime.fromtimestamp(file_data.st_mtime)
        
        if not(date):
            context['files'].append({'name' : file, 'ctime' : file_ctime, 'mtime' : file_mtime})
        elif context['date'].date() == file_ctime.date() or context['date'].date() == file_mtime.date():
            context['files'].append({'name' : file, 'ctime' : file_ctime, 'mtime' : file_mtime})



    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_path = os.path.join(settings.FILES_PATH, name)
    if os.path.exists(file_path):
        f = open(file_path, "r")
        content = f.read()

    else:
        content = "Указанный файл не существует"

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

