"""Platzigram views """
#Django
from django.http import HttpResponse

#Utilities
from datetime import datetime
from django.http import JsonResponse

def hello_world(request):

    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('oh, hi! Current server time is {now}'.format(now=str(now)))

def hi(request):
    
    res = {}
    res ['numbers'] = sorted(map(int, request.GET['numbers'].split(',')))
    
    return JsonResponse(res)