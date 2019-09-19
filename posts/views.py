from django.shortcuts import render
# Utilities
from datetime import datetime

# Create your views here.

posts = [
    {'title': 'Mont Blanc',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://picsum.photos/200/200/?image=1036',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
     },
    {'title': 'Via Lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/200/200/?image=903',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',

     },
    {'title': 'Nuevo auditorio',
     'user': {
         'name': 'Uriel ',
         'picture': 'https://picsum.photos/200/200/?image=1076',
     },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',

     },
]


def list_posts(request):

    return render(request, 'feed.html', {'posts':  posts})
