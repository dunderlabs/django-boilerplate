from django.test import TestCase, Client
from django.urls import reverse


class CoreTestIndexView(TestCase):

    def setUp(self):
        self.url = reverse('core:index')
        self.client = Client()

    def test_status_code_is_200(self):
        response = self.client.get(self.url)
        assert response.status_code == 200
