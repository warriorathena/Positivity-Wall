from django.urls import path
from .views import mur_view

urlpatterns = [
    path('', mur_view, name='mur'),
]
