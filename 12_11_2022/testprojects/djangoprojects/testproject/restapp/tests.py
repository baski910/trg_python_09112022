from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class BookTest(APITestCase):
    def test_create_title(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('restapp:books')
        data = {'booktitle': 'ruby','bookauthor':'matz'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('data'), data)