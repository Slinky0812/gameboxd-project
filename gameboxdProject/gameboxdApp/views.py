from django.shortcuts import render
from .models import Review


# Home view
def home(request):
    context = {
        'posts': Review.objects.all()
    }
    return render(request, 'gameboxdApp/home.html', context=context)


# About view
def about(request):
    context = {'title': 'About'}
    return render(request, 'gameboxdApp/about.html', context=context)