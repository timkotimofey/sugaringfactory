from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    BUTTON_LOGIN = (By.XPATH, '//*[@id="login"]/div/div[3]/a[1]')
