from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
	authors = serializers.SlugRelatedField(many = True, queryset=Author.objects.all(), slug_field ='name')
	class Meta:
		model = Book
		fields = '__all__'