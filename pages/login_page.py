from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def login(self, login, passwd):
        self.driver.find_by_id(LoginPageLocators.LOGIN_EMAIL_ID).fill(login)
        self.driver.find_by_id(LoginPageLocators.LOGIN_PASSWORD_ID).fill(passwd)
        self.driver.find_by_css(LoginPageLocators.LOGIN_BUTTON_CSS).click()
