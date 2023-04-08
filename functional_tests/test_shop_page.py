from .base import FunctionalTest
from selenium.webdriver.common.by import By


class MyShopTest(FunctionalTest):
    """тест страницы магазина"""

    def test_can_go_to_the_shop_page(self):
        """тест: пользователь может перейти на страницу магазина"""

        # Эдит переходит на сайт интернет магазина
        self.browser.get(self.live_server_url)

        # Она видит ссылку на страницу магазина
        self.browser.find_element(By.LINK_TEXT, 'Магазин').click()

        # Там она находит заголовок с надписью "Каталог товарів"
        title = self.browser.find_element(By.CSS_SELECTOR,
                                          'h1.section-header__title').text
        self.assertEqual('Каталог товарів', title)

