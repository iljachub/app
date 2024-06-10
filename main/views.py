from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context: dict[str, str] = {
        'title': 'Головна',
        'content': 'Це головна сторінка магазину ласощі',
        
      
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict[str, str] = {
        'title': 'Головна про Нас',
        'content': 'Це про нас',
        'text_on_page': "Тут усе що потрібно сказати"
        
      
    }

    return render(request, 'main/about.html', context)
 
 