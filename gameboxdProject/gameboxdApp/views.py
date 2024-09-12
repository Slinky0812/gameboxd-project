from django.shortcuts import render

posts = [
    {
        'author': 'Abdullah0812',
        'title': 'Elden Ring',
        'content': 'Great game',
        'date_posted': '27/08/2024'
    },
        {
        'author': 'Abdullah0812',
        'title': 'Tekken 8',
        'content': 'Boring game',
        'date_posted': '26/08/2024'
    }
]

# Home view
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'gameboxdApp/home.html', context=context)


# About view
def about(request):
    context = {'title': 'About'}
    return render(request, 'gameboxdApp/about.html', context=context)