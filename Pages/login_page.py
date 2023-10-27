from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "u")
    PASSWORD = (By.ID, "p")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn btn-bright btn-large btn-block")

    def navigate_to_login_page(self):
        self.browser.get(self.BASE_URL)

    def insert_correct_username(self):
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys("chivu1923@gmail.com")

    def insert_correct_password(self):
        password = self.browser.find_element(*self.PASSWORD)
        password.send_keys("Parola1234!@#$")

    def click_login_button(self):
        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()


