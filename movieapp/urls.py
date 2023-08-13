from django.urls import path
from . import views

urlpatterns = [
    path('movie/details/', views.MovieList.as_view()),
    path('movie/<int:pk>', views.MovieDetail.as_view())
]