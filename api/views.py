from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book, Author
from django.db import IntegrityError
import json, requests

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	http_method_names = ['get', 'post', 'patch', 'delete']

	def create(self, request, *args, **kwargs):
		validated_data = request.data
		authors = validated_data.pop('authors')
		book = Book(**validated_data)
		try:
			book.save()
		except IntegrityError:
			return Response({'status_code': 500, 'status':'failed', 'message': 'Book already exists'})
		for i in authors:
			var = Author.objects.filter(name = i).first()
			if var == None:
				var = Author.objects.create(name = i)
				var.save()
			book.authors.add(var)
		serializer = BookSerializer(book)
		resp = {
			'status_code': 201,
			'status': 'success',
			'data': [serializer.data]
		}
		return Response(resp)

	def retrieve(self, request, *args, **kwargs):
		instance = self.queryset.get(pk=kwargs.get('pk'))
		serializer = self.get_serializer(self.get_object())
		resp = {
			'status_code': 200,
			'status': 'success',
			'data': serializer.data
		}
		return Response(resp)

	def list(self, request, *args, **kwargs):
		name = self.request.query_params.get('name')
		country = self.request.query_params.get('country')
		year = self.request.query_params.get('year')
		publisher = self.request.query_params.get('publisher')
		obj = Book.objects.all()
		if name is not None:
			obj = obj.filter(name = name)
		if publisher is not None:
			obj = obj.filter(publisher = publisher)
		if country is not None:
			obj = obj.filter(country = country)
		if year is not None:
			obj = obj.filter(release_date__year = year)
		queryset = obj
		serializer = BookSerializer(queryset, many=True)
		resp = {
			'status_code': 200,
			'status': 'success',
			'data': serializer.data
		}
		return Response(resp)

	def partial_update(self, request, *args, **kwargs):
		instance = self.queryset.get(pk=kwargs.get('pk'))
		serializer = self.serializer_class(instance, data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		resp = {
			'status_code': 200,
			'status': 'success',
			'message': f'The book '+ instance.name +' was updated successfully',
			'data': serializer.data
		}
		return Response(resp)

	def destroy(self, request, *args, **kwargs):
		instance = self.queryset.get(pk=kwargs.get('pk'))
		serializer = self.get_serializer(self.get_object())
		super().destroy(request,*args, **kwargs)
		resp = {
			'status_code': 200,
			'status': 'success',
			'message': f'The book '+ instance.name +' was deleted successfully',
			'data': serializer.data
		}
		return Response(resp, status=status.HTTP_200_OK)


def iceAndFire(request):
	dat = requests.get("https://www.anapioficeandfire.com/api/books?name="+request.GET.get('name', ''))
	dat = json.loads(dat.text)
	resdat = []
	for i in dat:
		d = {
		'name' : i['name'],
		'isbn' : i['isbn'],
		'authors' : i['authors'],
		'number_of_pages' : i['numberOfPages'],
		'publisher' : i['publisher'],
		'country' : i['country'],
		'release_date': i['released'][:10]
		}
		resdat.append(d)
	resp = {
		'status_code': 200,
		'status': 'success',
		'data': resdat
	}
	return HttpResponse(json.dumps(resp))