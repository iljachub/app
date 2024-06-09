from typing import Any
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, Any] = {
        'title': 'Home',
        'content': 'Це головна сторінка магазину- HOME',
        'list': ['first, second'],
        'dict': {'first': 1},
        'is_authenticated': False
                 
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
 