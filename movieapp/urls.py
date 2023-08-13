from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.movie_list, name='movie'),
]