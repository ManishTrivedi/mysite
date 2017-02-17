from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from books.models import Publisher
from books.models import Author
from django.views.generic import ListView
from books.serializers import PublisherSerializer, AuthorSerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics

# This is a generic view example. This is like get all. Returns list of all objects for the model.
# Refer to Generic Views chapter in djangobooks.com
class PublisherList(ListView):
	model = Publisher
	context_object_name = 'my_favorite_publishers'
	# By default, if context name is not given then it is object_list or publisher_list i.e. modelname(in lower case)_list

def search(request):
	error = False
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html',
					  	  {'books' : books, 'query' : q})
	return render(request, 'search_form.html', {'error' : error})


#These two are examples of rest api. 
class PublisherListAPI(APIView):
	def get(self, request):
		publishers = Publisher.objects.all()
		serializer = PublisherSerializer(publishers, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = PublisherSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublisherDetail(APIView):
	serializer_class = PublisherSerializer
	def get_object(self, pk):
		try:
			return Publisher.objects.get(pk=pk)
		except Publisher.DoesNotExist:
			return Http404

	def get(self, request, pk):
		publisher = self.get_object(pk)
		serializer = PublisherSerializer(publisher)
		return Response(serializer.data)

	def put(self, request, pk):
		publisher = self.get_object(pk)
		serializer = PublisherSerializer(pk, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		publisher = self.get_object(pk)
		publisher.delete()
		return Response(status = status.HTTP_204_NP_CONTENT)

# The below APIs use viewset instead of views. 
# Viewsets are used in django rest as they provide default crud operations	
# Also, you dont need to set the urls explicitly. Is done used register.routes		

class AuthorViewSet(viewsets.ModelViewSet):
	queryset = Author.objects.all()
	serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookList(generics.ListAPIView):

	serializer_class = BookSerializer
	queryset = Book.objects.all()

	def get(self, request):

		## Note the use of `get_queryset()` instead of `self.queryset`
		#queryset - The queryset that should be used for returning objects from this view. 
		#Typically, you must either set this attribute, or override the get_queryset() method. 
		#If you are overriding a view method, it is important that you call get_queryset() instead of accessing this property directly, 
		#as queryset will get evaluated once, and those results will be cached for all subsequent requests.
		# http://www.django-rest-framework.org/api-guide/generic-views/

		pk_id = [1]
		#In order to get related table we use select_related
		#books = Book.objects.filter(pk__in=pk_id).select_related('publisher')
		books = Book.objects.filter(pk__in=pk_id)
		serializer = BookSerializer(books, many=True)
		return Response(serializer.data)





