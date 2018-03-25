from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class CoreTestIndexPage(StaticLiveServerTestCase):

    def setUp(self):
        self.url = "{}{}".format(self.live_server_url, reverse('core:index'))
        self.driver = WebDriver()
        self.driver.implicitly_wait(5)

    def test_index_page_is_working_message(self):
        self.driver.get(self.url)
        working_message = self.driver.find_element_by_xpath('//h1').text

        self.assertEquals('Django Boilerplate is working !', working_message)
