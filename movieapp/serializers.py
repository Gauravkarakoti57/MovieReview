from rest_framework import serializers
from .models import Movie, Actors

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'genre', 'category', 'buget', 'movie_release_location', 'release_date', 'actors']


class ActorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = ['id', 'name', 'gender', 'dob', 'address', 'contact', 'email']