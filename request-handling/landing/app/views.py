from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    req_param = request.GET.get('from-landing', 'none')
    if req_param == 'original':
        counter_click['original'] += 1
    elif req_param == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    req_param = request.GET.get('ab-test-arg', 'none')
    if req_param == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    elif req_param == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')
    else:
        return render_to_response('landing.html')



def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    original_conversion = 0
    test_conversion = 0

    print (counter_show, counter_click)
    if counter_show['original'] > 0:
        original_conversion = round(counter_click['original'] / counter_show['original'], 2)
    if counter_show['test'] > 0:
        test_conversion = round(counter_click['test'] / counter_show['test'], 2)


    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
