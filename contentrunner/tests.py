from django.http import response
from django.test.testcases import _AssertTemplateUsedContext
from django.urls import resolve
from django.test import TestCase
from contentrunner.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        # response = self.client.get('/')
        # self.assertTemplateUsed(response, 'home.html')
