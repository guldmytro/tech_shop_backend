from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class FunctionalTest(StaticLiveServerTestCase):
    """функциональный тест"""

    def setUp(self):
        """установка"""
        self.browser = webdriver.Chrome()
        self.live_server_url = 'http://localhost:5173'

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()
