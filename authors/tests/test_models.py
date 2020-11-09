import datetime
from django.test import TestCase

from authors.models import Author


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_author = Author.objects.create(
            full_name='test_billi foka',
            short_name='test_voivo',
            born=datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)
        )

    def test_object_name_is_full_name(self):
        expected_object_name = f'{self.test_author.full_name}'
        self.assertEqual(expected_object_name, str(self.test_author))

    def test_count_authors(self):
        db_count = Author.objects.all().count()
        self.assertEqual(1, db_count)

    def test_full_name_authors(self):
        db_author = self.test_author.full_name
        self.assertEqual('test_billi foka', db_author)

    def test_short_name_authors(self):
        db_author = self.test_author.short_name
        self.assertEqual('test_voivo', db_author)

    def test_born_authors(self):
        db_author = self.test_author.born.strftime("%Y-%m-%d")
        self.assertEqual('2015-10-09', db_author)
