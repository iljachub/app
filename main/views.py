from django.http import HttpResponse
from django.shortcuts import render

from goods.models import categories


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

def about(request):
    context: dict[str, str] = {
        'title': 'Як нас знайти',
        'content': 'Наші контакти',
        'text_on_page': "На сьогоднішній час ми не маємо свого магазину, але ми обов'зково зробимо його. Зв'язатися з нами можна за тел.0999639679 "
        
      
    }

    return render(request, 'main/about.html', context)
 
 