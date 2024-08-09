import logging

from django.core.files.storage import FileSystemStorage

from .forms import UserForm, ManyFieldsForm, ManyFieldsForWidget, ImageForm
from django.shortcuts import render
from .models import User

# Create your views here.

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # do somthing with variables
            logger.info(f'Получили {name=}, {email=}, {age=}')
    else:
        form = UserForm()

    return render(request, 'formsapp/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            # work with data
            logger.info(f'Get {form.cleaned_data=}')
    else:
        form = ManyFieldsForm()
    return render(request, 'formsapp/many_fields_form.html', {'form': form})


def many_fields_for_widget(request):
    if request.method == 'POST':
        form = ManyFieldsForWidget(request.POST)
        if form.is_valid():
            # work with data
            logger.info(f'Get {form.cleaned_data=}')
    else:
        form = ManyFieldsForWidget()
    return render(request, 'formsapp/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Error in data'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            user = User(name=name, email=email, age=age)
            user.save()
            message = 'User saved'
    else:
        form = UserForm()
        message = 'Fill the form'
    return render(request, 'formsapp/user_form.html',
                  {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'formsapp/upload_image.html', {'form': form})
