from django.test import TestCase, Client
from django.urls import reverse

class CompaniesTestCase(TestCase):
    def test_companies_valid(self):
        client = Client()
        response = client.get('/v1/companies/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"id": "1", "name": "MWNZ", "description": "..is awesome"}')

    def test_companies_invalid(self):
        client = Client()
        response = client.get('/v1/companies/5')
        self.assertEqual(response.status_code, 404)
