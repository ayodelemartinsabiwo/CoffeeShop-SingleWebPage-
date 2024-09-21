from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, response
from django.shortcuts import render
from .models import MenuItem


def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'home.html', {'menu_items': menu_items})
