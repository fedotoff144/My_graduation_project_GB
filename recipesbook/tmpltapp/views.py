from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render


# Create your views here.

def hello(request):
    return HttpResponse('Hello world from function!')


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello world from class!')


def year_post(request, year):
    text = ''
    # формируем статьи за год
    return HttpResponse(f'Posts from {year}<br>{text}')


class MonthPost(View):
    def get(self, year, month):
        text = ''
        # формируем статьи за год и месяц
        return HttpResponse(f'Posts from {month}/{year}<br>{text}')


def post_detail(request, year, month, slug):
    # формируем статьи за год и месяц по идентификатору, но пока без запросов к базе данных
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': 'Who is faster in create the lists in Python: list() or []',
        'content': 'In process of coding I thought about it',
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})
