from rest_framework import serializers
from books.models import Publisher
from books.models import Author
from books.models import Book
import rest_framework.validators
import pdb

class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Publisher
		fields = ('name', 'address', 'city', 'state_province', 'country', 'website')

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = ('first_name', 'last_name', 'email')	
	
# There is no need for validate method. However, when you call is_valid on any serializer,
# django internally calls few methods that validates the fields of the serializer. 
# validate() method is one of them. auth.py in ai-core uses this.
# Please refer to https://docs.djangoproject.com/en/1.10/ref/forms/validation/ for more details	
	def validate(self, attrs, **kwargs):
		n = attrs.get("email", None)
		pdb.set_trace()	
		return attrs	

#Below serialzer shows how we can use nested objects in serialization
#If we removew authors and publisher line from the below code, we will get just ids in the json output
#With the below two lines, we can get complete nested objects
#many=True is there in AuthorSerializer for obvious reasons. As there can be many authors

#By default nested serializers are read-only. 
#If you want to support write-operations to a nested serializer field you'll need to create
#create() and/or update() methods in order to explicitly specify how the child relationships should be saved.
#Please refer to http://www.django-rest-framework.org/api-guide/relations/ 'Writeable Nested Serializers' section
class BookSerializer(serializers.ModelSerializer):
#	authors = AuthorSerializer(many=True, read_only=True)
#	publisher = PublisherSerializer()

	class Meta:
		model = Book
		fields = ('title', 'authors', 'publisher', 'publication_date')

# If we just want to read nested objects and not save or update them as nested objects,
# we do not need to override the create or update method.
# I have not added authors here, coz when I do that, on the front end it is displayed that list are not supported
# in html right now i.e in the swagger like django rest api. I should directly test it with postman 
#	def create(self, validated_data):
#		publisher_data = validated_data.pop('publisher')
#		publisher = Publisher.objects.create(**publisher_data)
#		book = Book.objects.create(publisher=publisher, **validated_data)
#		return book		
