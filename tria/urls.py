from django.urls import path
from django.http import HttpResponse
from tria.views import my_view

# URL Configuration
urlpatterns = [
    path('form/', my_view, name='form_view'),
    path('success/', lambda request: HttpResponse("Form submitted successfully!")),
]