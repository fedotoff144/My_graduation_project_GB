from django.urls import path
from .views import user_form, many_fields_form, many_fields_for_widget, add_user, upload_image

urlpatterns = [
    path('user/', user_form, name='user_form'),
    path('mff/', many_fields_form, name='many_fields_form'),
    path('mffw/', many_fields_for_widget, name='many_fields_for_widget'),
    path('user/add/', add_user, name='add_user'),
    path('upload/', upload_image, name='upload_image'),
]
