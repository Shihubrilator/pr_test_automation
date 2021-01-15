from pypom import Page
from .locators import EditPageLocators as locators
import time


wait_time = 5
inner_name = 'тестовый проект для тестирования тестов'
name = 'тесты тесты'


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

    def set_template_url(self, changed_url):
        if self.driver.is_element_present_by_name(locators.URL_TEMPLATE_INPUT, wait_time):
            self.driver.find_by_name(locators.URL_TEMPLATE_INPUT)[0].fill(changed_url)

    def set_names(self):
        self.set_inner_name()
        self.set_name()

    def set_inner_name(self):
        if self.driver.is_element_present_by_name(locators.INNER_NAME_INPUT, wait_time):
            self.driver.find_by_name(locators.INNER_NAME_INPUT)[0].fill(inner_name)

    def set_name(self):
        if self.driver.is_element_present_by_name(locators.NAME_INPUT, wait_time):
            self.driver.find_by_name(locators.NAME_INPUT)[0].fill(name)

    def save_project_changes(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_by_text('Сохранить')[0].click()

    def reload(self):
        self.driver.reload()

    def should_be_changed_managers_name(self):
        self.should_be_changed_manager_name()
        self.should_be_changed_project_manager_name()

    def should_be_changed_manager_name(self):
        assert not self.driver.find_by_css(locators.MANAGER_INPUT + ' input[value="Админ"]', 5)
        #брать имя менеджера из базы
        assert self.driver.find_by_css(locators.MANAGER_INPUT + ' input[value="Бот"]', 5), \
            'manager name should be Бот but not'

    def should_be_changed_project_manager_name(self):
        assert self.driver.find_by_css(locators.PROJECT_MANAGER_INPUT + ' input[value="Бот"]', 5), \
            'project manager name should be Бот but not'

    def should_be_changed_url_template(self, changed_url):
        url_template = self.driver.find_by_name(locators.URL_TEMPLATE_INPUT).text
        assert url_template == changed_url, 'url template expected to be equal to ' + changed_url + 'but not'

    def should_be_changed_names(self):
        self.should_be_changed_inner_name()
        self.should_be_changed_name()

    def should_be_changed_inner_name(self):
        inner_name_value = self.driver.find_by_name(locators.INNER_NAME_INPUT)[0].value
        assert inner_name_value == inner_name, 'project InnerName expected to be equal to ' + inner_name + 'but not'

    def should_be_changed_name(self):
        name_value = self.driver.find_by_name(locators.NAME_INPUT)[0].value
        assert name_value == name, 'project Name expected to be equal to ' + name + 'but not'
