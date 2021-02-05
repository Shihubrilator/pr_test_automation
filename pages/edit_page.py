from pypom import Page
from .locators import EditPageLocators as locators
import time
import requests
import json


class EditPage(Page):
    wait_time = 5
    inner_name = 'тестовый проект для тестирования тестов'
    name = 'тесты тесты'
    xpctd_type = 'Ad-hoc'
    description = 'some nice description text'
    note = 'some annoying comments'
    device_type_text = 'Только ПК'
    device_type_default_text = 'Все устройства'
    device_type_show_text = 'Только мобильные'
    device_type_show_default_text = 'Наследовать от типа устройств'
    manager_text = 'Бот'
    manager_default_text = 'Админ'
    project_manager_text = 'Бот'
    project_manager_default_text = 'Админ'
    xpctd_category = 'Безалкогольные напитки'

    def set_settings(self, changed_url):
        self.set_manager()
        self.set_project_manager()
        self.set_template_url(changed_url)
        self.set_inner_name()
        self.set_name()
        self.set_type()
        self.set_sync()
        self.set_description()
        self.set_comments()
        self.set_device_type()
        self.set_device_type_show()
        self.set_multilinks()
        self.set_category()

    def should_be_changed_settings(self, changed_url):
        self.should_be_changed_manager_name()
        self.should_be_changed_project_manager_name()
        self.should_be_changed_url_template(changed_url)
        self.should_be_changed_inner_name()
        self.should_be_changed_name()
        self.should_be_changed_type()
        self.should_be_changed_sync()
        self.should_be_changed_description()
        self.should_be_changed_comments()
        self.should_be_changed_device_type()
        self.should_be_changed_device_type_show()
        self.should_be_changed_multilink()
        self.should_be_changed_category()

    def set_dropdown(self, input_locator, list_item_locator, li_number):
        if self.driver.is_element_present_by_css(input_locator, self.wait_time):
            self.driver.find_by_css(input_locator).first.click()
        if self.driver.is_element_present_by_css(list_item_locator, self.wait_time):
            time.sleep(0.5)
            self.driver.find_by_css(list_item_locator)[li_number].click()

    def set_input(self, input_locator, value):
        if self.driver.is_element_present_by_name(input_locator, self.wait_time):
            self.driver.find_by_name(input_locator)[0].fill(value)

    def set_toggle(self, toggle_locator):
        if self.driver.is_element_present_by_css(toggle_locator, self.wait_time):
            self.driver.find_by_css(toggle_locator).click()

    def set_type(self):
        if self.driver.is_element_present_by_css(locators.TYPE_INPUT, self.wait_time):
            self.driver.find_by_css(locators.TYPE_INPUT)[0].click()
        self.driver.find_by_css(locators.TYPE_LIST_ITEM)[2].click()

    def set_category(self):
        if self.driver.is_element_present_by_css('.rw-multiselect button.rw-multiselect-tag-btn'):
            self.driver.find_by_css('.rw-multiselect button.rw-multiselect-tag-btn').click()
        if self.driver.is_element_present_by_css('.rw-multiselect li'):
            time.sleep(0.5)
            self.driver.find_by_css('.rw-multiselect li')[3].click()

    def set_manager(self):
        self.set_dropdown(locators.MANAGER_INPUT, locators.MANAGER_LIST_ITEM, 4)

    def set_project_manager(self):
        self.set_dropdown(locators.PROJECT_MANAGER_INPUT, locators.PROJECT_MANAGER_LIST_ITEM, 4)

    def set_template_url(self, changed_url):
        self.set_input(locators.URL_TEMPLATE_INPUT, changed_url)

    def set_inner_name(self):
        self.set_input(locators.INNER_NAME_INPUT, self.inner_name)

    def set_name(self):
        self.set_input(locators.NAME_INPUT, self.name)

    def set_sync(self):
        self.set_toggle(locators.SYNC_TOGGLE)

    def set_description(self):
        self.set_input(locators.DESCRIPTION_INPUT, self.description)

    def set_comments(self):
        self.set_input(locators.COMMENTS_INPUT, self.note)

    def set_device_type(self):
        self.set_dropdown(locators.DEVICE_TYPE_INPUT, locators.DEVICE_TYPE_LIST_ITEM, 1)

    def set_device_type_show(self):
        self.set_dropdown(locators.DEVICE_TYPE_SHOW_INPUT, locators.DEVICE_TYPE_SHOW_LIST_ITEM, 2)

    def set_multilinks(self):
        self.set_toggle(locators.MULTILINKS_TOGGLE)

    def save_project_changes(self):
        self.driver.find_by_text('Сохранить')[0].click()

    def reload(self):
        self.driver.reload()

    def is_changed_dropdown(self, dropdown_locator, default_text, xpctd_text):
        assert not self.driver.find_by_css(dropdown_locator + ' input[value="' + default_text + '"]', 5)
        # брать ожидаемый текст из базы
        assert self.driver.find_by_css(dropdown_locator + ' input[value="' + xpctd_text + '"]', 5)

    def is_changed_input(self, input_locator, xpctd_text):
        assert self.driver.find_by_name(input_locator).text == xpctd_text

    def is_changed_toggle(self, toggle_locator):
        assert self.driver.is_element_present_by_css(toggle_locator + '--checked', self.wait_time)

    def should_be_changed_category(self):
        category = self.driver.find_by_css('.rw-multiselect li.rw-multiselect-tag').text
        assert category == self.xpctd_category

    def should_be_changed_type(self):
        selected_type = self.driver.find_by_css(locators.TYPE_INPUT).text
        assert selected_type == self.xpctd_type

    def should_be_changed_manager_name(self):
        self.is_changed_dropdown(locators.MANAGER_INPUT, self.manager_default_text, self.manager_text)

    def should_be_changed_project_manager_name(self):
        self.is_changed_dropdown(locators.PROJECT_MANAGER_INPUT,
                                 self.project_manager_default_text, self.project_manager_text)

    def should_be_changed_url_template(self, changed_url):
        self.is_changed_input(locators.URL_TEMPLATE_INPUT, changed_url)

    def should_be_changed_inner_name(self):
        self.is_changed_input(locators.INNER_NAME_INPUT, self.inner_name)

    def should_be_changed_name(self):
        self.is_changed_input(locators.NAME_INPUT, self.name)

    def should_be_changed_sync(self):
        self.is_changed_toggle(locators.SYNC_TOGGLE)

    def should_be_changed_description(self):
        self.is_changed_input(locators.DESCRIPTION_INPUT, self.description)

    def should_be_changed_comments(self):
        self.is_changed_input(locators.COMMENTS_INPUT, self.note)

    def should_be_changed_device_type(self):
        self.is_changed_dropdown(locators.DEVICE_TYPE_INPUT, self.device_type_default_text, self.device_type_text)

    def should_be_changed_device_type_show(self):
        self.is_changed_dropdown(locators.DEVICE_TYPE_SHOW_INPUT,
                                 self.device_type_show_default_text, self.device_type_show_text)

    def should_be_changed_multilink(self):
        self.is_changed_toggle(locators.MULTILINKS_TOGGLE)

    @staticmethod
    def set_default_settings(headers, config):
        request_url = config['pr']['url'] + 'api/v2/admin/panel/0/survey/' + str(config['pr']['project_id'])
        payload = json.dumps(config['pr']['default_project_settings'])
        requests.put(url=request_url, headers=headers, data=payload)
        # проверить, что запрос отправился
