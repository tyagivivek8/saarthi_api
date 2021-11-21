from django.db import models

class Author(models.Model):
	name = models.CharField(max_length = 50, unique = True)
	def __str__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length=100)
	isbn = models.CharField(unique=True, max_length=30)
	authors = models.ManyToManyField(Author)
	country = models.CharField(max_length=30)
	number_of_pages = models.IntegerField()
	publisher = models.CharField(max_length = 50)
	release_date = models.DateField()

	def __str__(self):
		return self.name

