
from django.test import TestCase
from django.test import Client


class CheapestTest(TestCase):
    def setUp(self):
        pass

    def get_200(self, input, result):
        c = Client()
        response = c.get('/api/v1/cheapest/', {
            'input': input
        })

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('cheapest', data.keys())
        self.assertEqual(data['cheapest'], result)


    def test_get_lakewood(self):
        self.get_200('Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)', 'Lakewood')

    def test_get_bridgewood(self):
        self.get_200('Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)', 'Bridgewood')

    def test_get_ridgewood(self):
        self.get_200('Reward: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)', 'Ridgewood')

    def test_get_400(self):
        c = Client()

        response = c.get('/api/v1/cheapest/', {
        })
        self.assertEqual(response.status_code, 400)
        
        response = c.get('/api/v1/cheapest/', {
            'input': 'Reguar: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
        })
        self.assertEqual(response.status_code, 400)