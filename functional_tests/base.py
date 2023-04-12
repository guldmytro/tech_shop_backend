from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class FunctionalTest(StaticLiveServerTestCase):
    """функциональный тест"""
    fixtures = ['products.json']
    port = 8000

    def setUp(self):
        """установка"""
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.live_frontend_server_url = 'http://localhost:5173'

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()
