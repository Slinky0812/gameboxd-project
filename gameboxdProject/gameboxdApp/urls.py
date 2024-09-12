from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gameboxd-home'),
    path('about/', views.about, name='gameboxd-about'),
]
