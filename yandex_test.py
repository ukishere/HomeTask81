import unittest
import requests

class Yandex_Test(unittest.TestCase):

    def test_smoke(self):
        parameters = {
            'key': '',
            'text': 'привет',
            'lang': ['ru-en']
        }
        response = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', parameters)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['text'], 'hi')

if __name__ == '__main__':
    unittest.main()