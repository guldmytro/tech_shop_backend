from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time


MAX_WAIT = 10


class MyShopTest(FunctionalTest):
    """тест страницы магазина"""

    def wait_for(self, fn):
        """ожидать"""
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_go_to_the_shop_page(self):
        """тест: пользователь может перейти на страницу магазина"""

        # Эдит переходит на сайт интернет магазина
        self.browser.get(self.live_server_url)

        # Она видит ссылку на страницу магазина
        self.browser.find_element(By.LINK_TEXT, 'Магазин').click()

        # Там она находит заголовок с надписью "Каталог товарів"
        title = self.wait_for(
            lambda: self.browser.find_element(By.CSS_SELECTOR,
                                          'h1.section-header__title'))
        self.assertEqual('Каталог товарів', title.text)

    def test_can_visit_singe_product_page(self):
        """тест: можно перейти на страницу пользователя"""

        # Эдит переходит на страницу магазина
        self.browser.get(f'{self.live_server_url}/shop')

        # Там она находит товар который её интересует и переходит на его
        # страницу
        product_link = self.wait_for(
            lambda: self.browser.find_element(By.CSS_SELECTOR,
                                                 '.product-item__title a'))
        product_link_text = product_link.text
        product_link.click()

        # Там заголовок товара соответствует
        single_product_title = self.wait_for(
            lambda: self.browser.find_element(By.CSS_SELECTOR,
                                              '.product-info__title')
        )
        self.assertEqual(product_link_text, single_product_title.text)


