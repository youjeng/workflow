#  from django.http import request, response 
from django.http import HttpRequest
from django.test.testcases import _AssertTemplateUsedContext
from django.urls import resolve
from django.test import TestCase
from contentrunner.views import home_page



class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        
        html = response.content.decode('utf8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>ContentRunner</title>', html)
        self.assertTrue(html.endswith('</html>'))