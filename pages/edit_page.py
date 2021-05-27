from pypom import Page
from .locators import EditPageLocators as locators
import requests
import json
from selenium.webdriver.common.keys import Keys
from .pr_fields import *


class EditPage(Page):
    def change_type(self, config):
        set_type(self.driver, locators.TYPE_INPUT, locators.TYPE_LIST_ITEM, 2, config['pr']['wait_time'])

    def change_category(self, config):
        set_category(self.driver, locators.CATEGORY_LIST, locators.CATEGORY_LIST_ITEM, config['pr']['wait_time'])

    def change_manager(self, config):
        set_dropdown(self.driver, locators.MANAGER_INPUT, locators.MANAGER_LIST_ITEM, 4, config['pr']['wait_time'])

    def change_project_manager(self, config):
        set_dropdown(self.driver, locators.PROJECT_MANAGER_INPUT,
                     locators.PROJECT_MANAGER_LIST_ITEM, 4, config['pr']['wait_time'])

    def change_template_url(self, config):
        set_input(self.driver, locators.URL_TEMPLATE_INPUT,
                  config['pr']['xpctd_settings']['url_template'], config['pr']['wait_time'])

    def change_inner_name(self, config):
        set_input(self.driver, locators.INNER_NAME_INPUT,
                  config['pr']['xpctd_settings']['inner_name'], config['pr']['wait_time'])

    def change_name(self, config):
        set_input(self.driver, locators.NAME_INPUT,
                  config['pr']['xpctd_settings']['name'], config['pr']['wait_time'])

    def change_sync(self, config):
        set_toggle(self.driver, locators.SYNC_TOGGLE, config['pr']['wait_time'])

    def change_description(self, config):
        set_input(self.driver, locators.DESCRIPTION_INPUT,
                  config['pr']['xpctd_settings']['description'], config['pr']['wait_time'])

    def change_comments(self, config):
        set_input(self.driver, locators.COMMENTS_INPUT,
                  config['pr']['xpctd_settings']['note'], config['pr']['wait_time'])

    def change_device_type(self, config):
        set_dropdown(self.driver, locators.DEVICE_TYPE_INPUT,
                     locators.DEVICE_TYPE_LIST_ITEM, 1, config['pr']['wait_time'])

    def change_device_type_show(self, config):
        set_dropdown(self.driver, locators.DEVICE_TYPE_SHOW_INPUT,
                     locators.DEVICE_TYPE_SHOW_LIST_ITEM, 2, config['pr']['wait_time'])

    def change_multilinks(self, config):
        set_toggle(self.driver, locators.MULTILINKS_TOGGLE, config['pr']['wait_time'])

    def change_status_time_and_cancel(self, config):
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_CELL, config['pr']['wait_time']).click()
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_INPUT_SHOW, config['pr']['wait_time']).click()
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_INPUT, config['pr']['wait_time']).type(Keys.BACKSPACE)
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_INPUT, config['pr']['wait_time']).type(Keys.BACKSPACE)
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_INPUT, config['pr']['wait_time']).type('42')
        self.driver.find_by_css('h3')[1].click()
        self.driver.find_by_css(locators.STATUS_CANCEL_CHANGES, config['pr']['wait_time']).click()

    def change_status_time(self, config):
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_CELL, config['pr']['wait_time']).click()
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_INPUT_SHOW, config['pr']['wait_time']).click()
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_INPUT, config['pr']['wait_time']).type(Keys.BACKSPACE)
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_INPUT, config['pr']['wait_time']).type(Keys.BACKSPACE)
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_INPUT, config['pr']['wait_time']).type('20')
        self.driver.find_by_css(locators.STATUS_SAVE_CHANGES, config['pr']['wait_time']).click()

    def should_be_changed_category(self, config):
        is_changed_category(self.driver, locators.CATEGORY_LIST_ITEM_SELECTED,
                            config['pr']['xpctd_settings']['category'], config['pr']['wait_time'])

    def should_be_changed_type(self, config):
        is_changed_type(self.driver, config['pr']['xpctd_settings']['type'], config['pr']['wait_time'])

    def should_be_not_changed_status_time(self, config):
        text = self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_CELL, config['pr']['wait_time']).text
        xpctd_text = '10'
        assert text == xpctd_text, 'Status time is "' + text + '", but expected "' + xpctd_text + '"'

    def should_be_changed_status_time(self, config):
        text = self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_CELL, config['pr']['wait_time']).text
        xpctd_text = '20'
        assert text == xpctd_text, 'Status time is "' + text + '", but expected "' + xpctd_text + '"'

    def should_be_changed_manager_name(self, config):
        is_changed_dropdown(self.driver, locators.MANAGER_INPUT, config['pr']['default_settings']['manager'],
                            config['pr']['xpctd_settings']['manager'], config['pr']['wait_time'])

    def should_be_changed_project_manager_name(self, config):
        is_changed_dropdown(self.driver, locators.PROJECT_MANAGER_INPUT,
                            config['pr']['default_settings']['project_manager'],
                            config['pr']['xpctd_settings']['project_manager'], config['pr']['wait_time'])

    def should_be_changed_url_template(self, config):
        is_changed_input(self.driver, config['pr']['xpctd_settings']['url_template'], config['pr']['wait_time'])

    def should_be_changed_inner_name(self, config):
        is_changed_input(self.driver, config['pr']['xpctd_settings']['inner_name'], config['pr']['wait_time'])

    def should_be_changed_name(self, config):
        is_changed_input(self.driver, config['pr']['xpctd_settings']['name'], config['pr']['wait_time'])

    def should_be_changed_sync(self, config):
        is_changed_toggle(self.driver, locators.SYNC_TOGGLE, config['pr']['wait_time'])

    def should_be_changed_description(self, config):
        is_changed_input(self.driver, config['pr']['xpctd_settings']['description'], config['pr']['wait_time'])

    def should_be_changed_comments(self, config):
        is_changed_input(self.driver, config['pr']['xpctd_settings']['note'], config['pr']['wait_time'])

    def should_be_changed_device_type(self, config):
        is_changed_dropdown(self.driver, locators.DEVICE_TYPE_INPUT,
                            config['pr']['default_settings']['device_type_text'],
                            config['pr']['xpctd_settings']['device_type_text'], config['pr']['wait_time'])

    def should_be_changed_device_type_show(self, config):
        is_changed_dropdown(self.driver, locators.DEVICE_TYPE_SHOW_INPUT,
                            config['pr']['default_settings']['device_type_show_text'],
                            config['pr']['xpctd_settings']['device_type_show_text'], config['pr']['wait_time'])

    def should_be_changed_multilink(self, config):
        is_changed_toggle(self.driver, locators.MULTILINKS_TOGGLE, config['pr']['wait_time'])

    def should_be_collector_template_url(self):
        time.sleep(1)
        assert '/collectortemplates/' in self.driver.url, 'Should be collector template url, but not'

    def save_project_changes(self):
        self.driver.find_by_text('Сохранить')[0].click()

    def reload(self):
        self.driver.reload()

    def set_default_settings(self, headers, config):
        self.set_default_project_settings(config, headers)
        self.set_default_status_settings(config, headers)
        self.delete_last_collector_template(config, headers)

    @staticmethod
    def set_default_project_settings(config, headers):
        request_url = config['pr']['url'] + 'api/v2/admin/panel/0/survey/' + str(config['pr']['project_id'])
        payload = json.dumps(config['pr']['default_settings_json'])
        requests.put(url=request_url, headers=headers, data=payload)

    @staticmethod
    def set_default_status_settings(config, headers):
        request_url = config['pr']['url'] + 'api/v2/admin/panel/0/survey/' + \
                      str(config['pr']['project_id']) + '/SurveyFinishStatus'
        payload = {
            'AverageTime': '',
            'BackwardUri': 'http://qa.expertnoemnenie.ru/[hz]?status=92',
            'Id': 765277187,
            'Name': 'ScreenOut',
            'StatusCode': 92,
            'StatusType': 92,
            'SurveyId': config['pr']['project_id']
        }
        additional_headers = dict(headers)
        additional_headers['Content-Type'] = 'application/x-www-form-urlencoded'
        additional_headers['Content-Length'] = '168'
        requests.put(url=request_url, headers=additional_headers, data=payload)

    @staticmethod
    def delete_last_collector_template(config, headers):
        param = {
            'page': 1,
            'pageSize': 20,
            'filter': 'Deleted~eq~false~and~SurveyId~eq~' + str(config['pr']['project_id'])
        }
        request_url = config['pr']['url'] + 'api/v2/admin/panel/0/collectorTemplates'
        r = requests.get(url=request_url, headers=headers, params=param)
        data = r.json()['Data']
        if len(data) > 1:
            request_url = config['pr']['url'] + 'api/v2/admin/panel/0/collectortemplates/' + str(data[0]['Id'])
            requests.delete(url=request_url, headers=headers)

    def add_collector_template(self, config):
        self.driver.find_by_css(locators.ADD_COLLECTOR_TEMPLATE_BUTTON, config['pr']['wait_time'])[0].click()
        self.driver.find_by_css(locators.COLLECTOR_TEMPLATE_NAME_INPUT, config['pr']['wait_time']). \
            type(config['pr']['xpctd_c_tmplt_settings']['name'])
        self.driver.find_by_css(locators.COLLECTOR_TEMPLATE_NAME_CONFIRM_BUTTON, config['pr']['wait_time']).click()
