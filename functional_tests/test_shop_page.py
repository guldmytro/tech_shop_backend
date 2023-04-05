from .base import FunctionalTest


class MyShopTest(FunctionalTest):
    """тест страницы магазина"""

    def test_can_go_to_the_shop_page(self):
        """тест: пользователь может перейти на страницу магазина"""

        # Эдит переходит на сайт интернет магазина
        self.browser.get(self.live_server_url)
