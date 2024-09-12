from django.shortcuts import render
from django.http import HttpResponse

# Home view
def home(request):
    return HttpResponse('<h1>Home</h1>')


# About view
def about(request):
    return HttpResponse('<h1>About</h1>')