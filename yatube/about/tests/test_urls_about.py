from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class StaticURLTests(TestCase):

    def test_static_pages_abs(self):
        static_urls = (
            '/about/author/',
            '/about/tech/'
        )
        for url in static_urls:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)
