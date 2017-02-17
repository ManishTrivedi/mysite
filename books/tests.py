from django.test import TestCase
from books.views import BookViewSet
import json
import pdb

# Create your tests here.
class SimpleTest(TestCase):
	headers = {}

	def setUp(self):
		headers = {
			'Device' : 'a48af651ddc200dd354a3d8c5fce54bb',
			'Authorization' : 'token T8G00WTAUA7C8ATVKET4LW4BZ06T61NXPQG9SR5U',
			'Type' : '8',
			'Appid' : '1',
			'Public' : 'olivia.recruiting.ai',
			'Language' : 'en'
		}
		self.headers = headers

	def test_get_books(self):
		response = self.client.get('/books/')	
		self.assertEqual(response.status_code, 200)

	def test_post_author(self):

		author = {
			'first_name' : 'Jason',
			'last_name' : 'Bourne',
			'email' : 'jas@gmail.com'
		}

		pdb.set_trace()
		response = self.client.post('/authors/', json.dumps(author), 'application/json', self.headers)
		
		self.assertEqual(response.status_code, 201)