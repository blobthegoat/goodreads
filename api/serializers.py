from pickletools import read_long1

from books.models import CustomUser, Book, Rating
from rest_framework import serializers

class BookSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='rating-detail',
        read_only=True
    )
    class Meta:
        model = Book
        fields = ['url', 'title', 'title_long', 'description', 'date_published', 'author', 'reviews']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='rating-detail',
        read_only=True
    )
    class Meta:
        model = CustomUser
        fields = ['url', 'first_name', 'last_name', 'reviews']


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ['url', 'book', 'user', 'body', 'score']
    

