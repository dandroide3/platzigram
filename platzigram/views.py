"""Platzigram views """
#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
from django.http import JsonResponse
import json

def hello_world(request):

    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('oh, hi! Current server time is {now}'.format(now=str(now)))

def sorted_integers(request):
    # primer metodo
    ''' res = {}
    res ['numbers'] = sorted(map(int, request.GET['numbers'].split(',')))
    
    return JsonResponse(res) '''

    #metodo usado en la clase
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
		'status': 'ok',
		'numbers': sorted_ints,
		'message': 'Integers sorted successfully.'
	}
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    ''' Return a greeeting '''

    if age < 12:
        message = 'Sorry {}, you not allowed here'.format(name)
    else:
        message = 'Hello, {}! welcome to plaztigram'.format(name)
    return HttpResponse(message)