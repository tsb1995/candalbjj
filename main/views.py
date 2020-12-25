from django.shortcuts import render, redirect
from django.core.mail import send_mail as sm
import requests
import json
import time
from . GooglePlaces import *

# Create your views here.

def index(request):
    # # For using google places api if JS fails
    # api = GooglePlaces("INSERT API KEY HERE")
    # fields = ['name', 'website', 'rating', 'review']
    # details = api.get_place_details("ChIJe-_o2Sgp3YARE02PnQhDX2A", fields)
    # print(details)

    context = {
        'nbar': 'home',
    }

    return render(request, "index.html", context)

def about(request):
    context = {
        'nbar': 'about',
    }
    
    return render(request, "about.html", context)

def contact(request):
    context = {
        'nbar': 'contact',
    }
    
    return render(request, "contact.html", context)

def instructors(request):
    context = {
        'nbar': 'instructors',
    }
    
    return render(request, "instructors.html", context)

def send_mail(request):

    name = request.GET['name']
    phone = request.GET['phone']
    email = request.GET['email']

    res1 = sm(
        subject = "Candal's Martial Arts Contact",
        message = "Hey! Thanks for contacting us at Candal's Martial Arts. We will be getting back to you as soon as possible to bring more information on our Martial Arts Classes",
        from_email = 'tsb1995@gmail.com',
        recipient_list = ['tsb1995@gmail.com'],
        fail_silently=False,
    )

    res2 = sm(
        subject = "New Site Contact",
        message = "A possible new student has contacted us. Their name is {}, phone number {}, and email {}.".format(name, phone, email),
        from_email = 'tsb1995@gmail.com',
        recipient_list = ['tsb1995@gmail.com'],
        fail_silently=False,
    )

    context = {
        'nbar': 'home',
    }

    return redirect('index')