from django.test import TestCase
from Bares.models import Tapa, Bar, UserProfile
from django.test import Client



class BarTestCase(TestCase):	
	def test_index(self):
		response = self.client.get('/Bares/')
		self.assertEqual(response.status_code, 200)

	def test_visitas(self):
		response = self.client.get('/Bares/visitas/')
		self.assertEqual(response.status_code, 200)
		
	def test_about(self):
		response = self.client.get('/Bares/about/')
		self.assertEqual(response.status_code, 200)
		
	def test_login(self):
		response = self.client.get('/Bares/login/')
		self.assertEqual(response.status_code, 200)

