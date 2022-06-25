from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('info', views.info, name='info'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('records', views.records, name='records'),
]
