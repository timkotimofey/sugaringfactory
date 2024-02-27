import time

from locators.login_page_locators import LoginLocators
from pages.base_page import BasePage


class LoginPageType(BasePage):
    locators = LoginLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.EMAIL).send_keys('timkotimofeytest@gmail.com')
        self.element_is_visible(self.locators.PASSWORD).send_keys('1984Timofeus1984!')
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()


