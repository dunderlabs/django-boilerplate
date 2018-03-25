from django.test import TestCase, Client


class CoreTestIndexView(TestCase):

    def setUp(self):
        self.url = '/'
        self.client = Client()
        self.response = self.client.get(self.url)

    def test_index_view_response_status(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_view_template(self):
        self.assertTemplateUsed(self.response, 'base.html')
        self.assertTemplateUsed(self.response, 'core/index.html')
