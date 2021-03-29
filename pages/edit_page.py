from pypom import Page
from .locators import EditPageLocators as locators
import time
import requests
import json


class EditPage(Page):
    def set_settings(self, config):
        self.set_manager(config)
        self.set_project_manager(config)
        self.set_template_url(config)
        self.set_inner_name(config)
        self.set_name(config)
        self.set_type(config)
        self.set_sync(config)
        self.set_description(config)
        self.set_comments(config)
        self.set_device_type(config)
        self.set_device_type_show(config)
        self.set_multilinks(config)
        self.set_category(config)

    def set_dropdown(self, input_locator, list_item_locator, li_number, config):
        if self.driver.is_element_present_by_css(input_locator, config['pr']['wait_time']):
            self.driver.find_by_css(input_locator).first.click()
        if self.driver.is_element_present_by_css(list_item_locator, config['pr']['wait_time']):
            time.sleep(0.5)
            self.driver.find_by_css(list_item_locator)[li_number].click()

    def set_input(self, input_locator, value, config):
        if self.driver.is_element_present_by_name(input_locator, config['pr']['wait_time']):
            self.driver.find_by_name(input_locator)[0].clear()
            self.driver.find_by_name(input_locator)[0].fill(value)

    def set_toggle(self, toggle_locator, config):
        if self.driver.is_element_present_by_css(toggle_locator, config['pr']['wait_time']):
            self.driver.find_by_css(toggle_locator).click()

    def set_type(self, config):
        if self.driver.is_element_present_by_css(locators.TYPE_INPUT, config['pr']['wait_time']):
            self.driver.find_by_css(locators.TYPE_INPUT)[0].click()
        self.driver.find_by_css(locators.TYPE_LIST_ITEM)[2].click()

    def set_category(self, config):
        if self.driver.is_element_present_by_css(locators.CATEGORY_LIST, config['pr']['wait_time']):
            self.driver.find_by_css(locators.CATEGORY_LIST).click()
        if self.driver.is_element_present_by_css(locators.CATEGORY_LIST_ITEM, config['pr']['wait_time']):
            time.sleep(0.5)
            self.driver.find_by_css(locators.CATEGORY_LIST_ITEM)[3].click()

    def set_manager(self, config):
        self.set_dropdown(locators.MANAGER_INPUT, locators.MANAGER_LIST_ITEM, 4, config)

    def set_project_manager(self, config):
        self.set_dropdown(locators.PROJECT_MANAGER_INPUT, locators.PROJECT_MANAGER_LIST_ITEM, 4, config)

    def set_template_url(self, config):
        self.set_input(locators.URL_TEMPLATE_INPUT, config['pr']['xpctd_settings']['url_template'], config)

    def set_inner_name(self, config):
        self.set_input(locators.INNER_NAME_INPUT, config['pr']['xpctd_settings']['inner_name'], config)

    def set_name(self, config):
        self.set_input(locators.NAME_INPUT, config['pr']['xpctd_settings']['name'], config)

    def set_sync(self, config):
        self.set_toggle(locators.SYNC_TOGGLE, config)

    def set_description(self, config):
        self.set_input(locators.DESCRIPTION_INPUT, config['pr']['xpctd_settings']['description'], config)

    def set_comments(self, config):
        self.set_input(locators.COMMENTS_INPUT, config['pr']['xpctd_settings']['note'], config)

    def set_device_type(self, config):
        self.set_dropdown(locators.DEVICE_TYPE_INPUT, locators.DEVICE_TYPE_LIST_ITEM, 1, config)

    def set_device_type_show(self, config):
        self.set_dropdown(locators.DEVICE_TYPE_SHOW_INPUT, locators.DEVICE_TYPE_SHOW_LIST_ITEM, 2, config)

    def set_multilinks(self, config):
        self.set_toggle(locators.MULTILINKS_TOGGLE, config)

    def is_changed_dropdown(self, dropdown_locator, default_text, xpctd_text, config):
        assert not self.driver.find_by_css(dropdown_locator + ' input[value="' + default_text + '"]',
                                           config['pr']['wait_time']), 'Dropdown is not changed'
        assert self.driver.find_by_css(dropdown_locator + ' input[value="' + xpctd_text + '"]',
                                       config['pr']['wait_time']), 'Dropdown is not found'

    def is_changed_input(self, xpctd_text):
        assert self.driver.is_element_present_by_value(xpctd_text), 'Input with text "' + xpctd_text + '" is not found'

    def is_changed_toggle(self, toggle_locator, config):
        assert self.driver.is_element_present_by_css(toggle_locator + '--checked', config['pr']['wait_time']), \
            'Element "' + toggle_locator + '--checked" is not found'

    def should_be_changed_category(self, config):
        category = self.driver.find_by_css(locators.CATEGORY_LIST_ITEM_SELECTED).text
        xpctd_category = config['pr']['xpctd_settings']['category'] + ' ×'
        assert category == xpctd_category, 'Category "' + category + '" expected to be "' + xpctd_category + '"'

    def should_be_changed_type(self, config):
        assert self.driver.is_element_present_by_text(config['pr']['xpctd_settings']['type'],
                                                      config['pr']['wait_time']), 'Type is not changed'

    def should_be_changed_manager_name(self, config):
        self.is_changed_dropdown(locators.MANAGER_INPUT,
                                 config['pr']['default_settings']['manager'],
                                 config['pr']['xpctd_settings']['manager'], config)

    def should_be_changed_project_manager_name(self, config):
        self.is_changed_dropdown(locators.PROJECT_MANAGER_INPUT,
                                 config['pr']['default_settings']['project_manager'],
                                 config['pr']['xpctd_settings']['project_manager'], config)

    def should_be_changed_url_template(self, config):
        self.is_changed_input(config['pr']['xpctd_settings']['url_template'])

    def should_be_changed_inner_name(self, config):
        self.is_changed_input(config['pr']['xpctd_settings']['inner_name'])

    def should_be_changed_name(self, config):
        self.is_changed_input(config['pr']['xpctd_settings']['name'])

    def should_be_changed_sync(self, config):
        self.is_changed_toggle(locators.SYNC_TOGGLE, config)

    def should_be_changed_description(self, config):
        self.is_changed_input(config['pr']['xpctd_settings']['description'])

    def should_be_changed_comments(self, config):
        self.is_changed_input(config['pr']['xpctd_settings']['note'])

    def should_be_changed_device_type(self, config):
        self.is_changed_dropdown(locators.DEVICE_TYPE_INPUT,
                                 config['pr']['default_settings']['device_type_text'],
                                 config['pr']['xpctd_settings']['device_type_text'], config)

    def should_be_changed_device_type_show(self, config):
        self.is_changed_dropdown(locators.DEVICE_TYPE_SHOW_INPUT,
                                 config['pr']['default_settings']['device_type_show_text'],
                                 config['pr']['xpctd_settings']['device_type_show_text'], config)

    def should_be_changed_multilink(self, config):
        self.is_changed_toggle(locators.MULTILINKS_TOGGLE, config)

    def save_project_changes(self):
        self.driver.find_by_text('Сохранить')[0].click()

    def reload(self):
        self.driver.reload()

    @staticmethod
    def set_default_settings(headers, config):
        request_url = config['pr']['url'] + 'api/v2/admin/panel/0/survey/' + str(config['pr']['project_id'])
        payload = json.dumps(config['pr']['default_settings_json'])
        requests.put(url=request_url, headers=headers, data=payload)
        # проверить, что запрос отправился
