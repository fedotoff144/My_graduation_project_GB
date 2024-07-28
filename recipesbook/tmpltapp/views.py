from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


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


def my_view(request):
    context = {"name": "John"}
    return render(request, 'tmpltapp/my_template.html', context)


class TemplIf(TemplateView):
    template_name = 'tmpltapp/templ_if.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello World!'
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'желтый',
        'знать': 'зеленый',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'tmpltapp/temp_for.html', context)


def index(request):
    return render(request, 'tmpltapp/index.html')


def about(request):
    return render(request, 'tmpltapp/about.html')
