from base_page import BasePage


class IndexPage(BasePage):

    def check_current_url(self):
        expected_url = "https://www.price.ro/index.php?action=account"
        actual_url = self.browser.current_url
        assert expected_url == actual_url
