from pypom import Page
from .locators import EditPageLocators as locators
import time


class EditPage(Page):
    def set_manager(self):
        if self.driver.is_element_present_by_css(locators.MANAGER_INPUT):
            self.driver.find_by_css(locators.MANAGER_INPUT).first.click()
        if self.driver.is_element_present_by_css(locators.MANAGER_LIST_ITEM):
            time.sleep(1)
            self.driver.find_by_css(locators.MANAGER_LIST_ITEM)[4].click()

    def set_project_manager(self):
        if self.driver.is_element_present_by_css(locators.PROJECT_MANAGER_INPUT):
            self.driver.find_by_css(locators.PROJECT_MANAGER_INPUT).first.click()
        if self.driver.is_element_present_by_css(locators.PROJECT_MANAGER_LIST_ITEM):
            time.sleep(1)
            self.driver.find_by_css(locators.PROJECT_MANAGER_LIST_ITEM)[4].click()
