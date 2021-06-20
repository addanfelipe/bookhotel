
from django.test import TestCase
from django.test import Client

class CheapestTest(TestCase):
    def setUp(self):
      pass

    def test_(self):
      c = Client()
      request = c.get('/api/v1/cheapest/', {
        'input': 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
      })
      response = request.json()
      self.assertIn('cheapest', response.keys())
      self.assertEqual(response['cheapest'], 'Lakewood')
