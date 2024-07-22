from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    return HttpResponse('Hello world!')


# def about(request):
#     return HttpResponse('About Us')

def about(request):
    try:
        # some code that might raise an exception
        res = 1/0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('Oops, page was stolen')
    else:
        logger.debug('About page accessed')
        return HttpResponse('This is about page')
