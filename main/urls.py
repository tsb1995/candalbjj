from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('instructors', views.instructors, name='instructors'),
    path('send_mail', views.send_mail, name='send_mail'),
]