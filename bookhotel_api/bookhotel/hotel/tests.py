
from django.test import TestCase
from django.test import Client

class CheapestTest(TestCase):
    def setUp(self):
      pass

    def test_(self):
      c = Client()
      response = c.get('/api/v1/cheapest/', {
        'input': 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
      })
      self.assertEqual(response.status_code, 200)
      
      data = response.json()
      self.assertIn('cheapest', data.keys())
      self.assertEqual(data['cheapest'], 'Lakewood')
