from pypom import Page
from .locators import EditPageLocators as locators
import time


wait_time = 5


class EditPage(Page):
    def set_managers(self):
        self.set_manager()
        self.set_project_manager()

    def set_manager(self):
        if self.driver.is_element_present_by_css(locators.MANAGER_INPUT, wait_time):
            self.driver.find_by_css(locators.MANAGER_INPUT).first.click()
        if self.driver.is_element_present_by_css(locators.MANAGER_LIST_ITEM, wait_time):
            time.sleep(0.5)
            self.driver.find_by_css(locators.MANAGER_LIST_ITEM)[4].click()

    def set_project_manager(self):
        if self.driver.is_element_present_by_css(locators.PROJECT_MANAGER_INPUT, wait_time):
            self.driver.find_by_css(locators.PROJECT_MANAGER_INPUT).first.click()
        if self.driver.is_element_present_by_css(locators.PROJECT_MANAGER_LIST_ITEM, wait_time):
            time.sleep(0.5)
            self.driver.find_by_css(locators.PROJECT_MANAGER_LIST_ITEM)[4].click()

    def save_project_changes(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_by_text('Сохранить')[0].click()

    def reload(self):
        self.driver.reload()

    def should_be_changed_managers_name(self):
        self.should_be_changed_manager_name()
        self.should_be_changed_project_manager_name()

    def should_be_changed_manager_name(self):
        assert self.driver.find_by_css(locators.MANAGER_INPUT + ' input[value="Бот"]', 5), \
            'manager name should be Бот but not'

    def should_be_changed_project_manager_name(self):
        assert self.driver.find_by_css(locators.PROJECT_MANAGER_INPUT + ' input[value="Бот"]', 5), \
            'project manager name should be Бот but not'
