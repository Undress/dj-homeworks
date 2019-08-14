import datetime
from django import template


register = template.Library()


@register.filter
def format_date(value):
	

	time_diff = (datetime.datetime.now() - datetime.datetime.fromtimestamp(value))

	if time_diff.days > 0:
		result = datetime.date.fromtimestamp(value).isoformat()
	elif (time_diff.seconds / 60) < 10:
		result = 'только что'
	elif (time_diff.seconds / 60) >= 10 and (time_diff.seconds / 60) < 1440:
		result = f'{round(time_diff.seconds / 3600)} часов назад'
		

	return result


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):

	if value < -5:
		return "все плохо"
	elif value >= -5 and value < 5:
		return "нейтрально"
	elif value >= 5:
		return "хорошо"
	else:
		return value

@register.filter
def format_num_comments(value):
    
    if value == 0:
    	return "Оставьте комментарий"
    elif value >= 0 and value < 50:
    	return value
    elif value >= 50:
    	return "50+"


@register.filter
def format_selfText(value, args):

	result_list = []
	text_list = value.split(' ')
	if len(text_list) > 2 * args:
		result_list.append(' '.join(text_list[:args]))
		result_list.append('...')
		result_list.append(' '.join(text_list[-args:]))
		result = ' '.join(result_list)
	else:
		result = value

	return result