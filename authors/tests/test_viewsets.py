from django.test import TestCase
from django.urls import reverse
import datetime

from authors.models import Author
from authors.api.viewsets import AuthorViewSet


class  AuthorViewSetTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_author = Author.objects.create(
            full_name='test_erfe effe',
            short_name='test_vweweo',
            born=datetime.datetime(2012, 10, 9, 23, 55, 59, 322480)
        )
        cls.test_author.save()

    def test_url_api(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_url_authors(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, 200)

    def test_count_authors(self):
        response = self.client.get('/api/authors/')
        response_count = response.data.get('count')
        self.assertEqual(response_count, 1)

    def test_full_name_authors(self):
        response = self.client.get('/api/authors/')
        response_author = response.data.get('results')[0]['full_name']
        self.assertEqual(response_author, 'test_erfe effe')

    def test_short_name_authors(self):
        response = self.client.get('/api/authors/')
        response_author = response.data.get('results')[0]['short_name']
        self.assertEqual(response_author, 'test_vweweo')

    def test_born_authors(self):
        response = self.client.get('/api/authors/')
        response_author = response.data.get('results')[0]['born']
        self.assertEqual(response_author, '2012-10-09')
