import time
from conftest import driver
from pages.base_page import BasePage
from pages.login_page import LoginPageType




class TestLogin:
    class TestLoginType:

        def test_login_typing(self, driver):
            login_page = LoginPageType(driver, 'https://test.sugaringfactory.com/index.php?route=account%2Flogin')
            login_page.open()
            login_page.fill_all_fields()
            time.sleep(5)

