from pypom import Page
from .locators import LoginPageLocators


class LoginPage(Page):
    def login(self, login, passwd):
        self.driver.find_by_id(LoginPageLocators.LOGIN_EMAIL_ID).fill(login)
        self.driver.find_by_id(LoginPageLocators.LOGIN_PASSWORD_ID).fill(passwd)
        self.driver.find_by_css(LoginPageLocators.LOGIN_BUTTON_CSS).click()
