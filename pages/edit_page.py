from .base_page import BasePage
from .locators import EditPageLocators as locators
from selenium.webdriver.common.keys import Keys
import requests
import json
import time


class EditPage(BasePage):
    def change_type(self, li_num, wt):
        self.set_type(locators.TYPE_INPUT, locators.TYPE_LIST_ITEM, li_num, wt)

    def change_category(self, wt):
        self.set_category(locators.CATEGORY_LIST, locators.CATEGORY_LIST_ITEM, wt)

    def change_manager(self, li_num, wt):
        self.set_dropdown(locators.MANAGER_INPUT, locators.MANAGER_LIST_ITEM, li_num, wt)

    def change_project_manager(self, li_num, wt):
        self.set_dropdown(locators.PROJECT_MANAGER_INPUT, locators.PROJECT_MANAGER_LIST_ITEM, li_num, wt)

    def change_template_url(self, xpctd_url, wt):
        self.set_input(locators.URL_TEMPLATE_INPUT, xpctd_url, wt)

    def change_inner_name(self, xpctd_inner_name, wt):
        self.set_input(locators.INNER_NAME_INPUT, xpctd_inner_name, wt)

    def change_name(self, xpctd_name, wt):
        self.set_input(locators.NAME_INPUT, xpctd_name, wt)

    def change_sync(self, wt):
        self.set_toggle(locators.SYNC_TOGGLE, wt)

    def change_description(self, xpctd_description, wt):
        self.set_input(locators.DESCRIPTION_INPUT, xpctd_description, wt)

    def change_comments(self, xpctd_note, wt):
        self.set_input(locators.COMMENTS_INPUT, xpctd_note, wt)

    def change_device_type(self, li_num, wt):
        self.set_dropdown(locators.DEVICE_TYPE_INPUT, locators.DEVICE_TYPE_LIST_ITEM, li_num, wt)

    def change_device_type_show(self, li_num, wt):
        self.set_dropdown(locators.DEVICE_TYPE_SHOW_INPUT, locators.DEVICE_TYPE_SHOW_LIST_ITEM, li_num, wt)

    def change_multilinks(self, wt):
        self.set_toggle(locators.MULTILINKS_TOGGLE, wt)

    def change_status_time_and_cancel(self, value, wt):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_CELL, wt).click()
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_INPUT_SHOW, wt).click()
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_INPUT, wt).type(Keys.BACKSPACE)
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_INPUT, wt).type(Keys.BACKSPACE)
        self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_INPUT, wt).type(str(value))
        self.driver.find_by_css('h3')[1].click()
        self.driver.find_by_css(locators.STATUS_CANCEL_CHANGES, wt).click()

    def change_status_time(self, value, wt):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_CELL, wt).click()
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_INPUT_SHOW, wt).click()
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_INPUT, wt).type(Keys.BACKSPACE)
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_INPUT, wt).type(Keys.BACKSPACE)
        self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_INPUT, wt).type(str(value))
        self.driver.find_by_css(locators.STATUS_SAVE_CHANGES, wt).click()

    def should_be_changed_category(self, xpctd_category, wt):
        self.is_changed_category(locators.CATEGORY_LIST_ITEM_SELECTED, xpctd_category, wt)

    def should_be_changed_type(self, xpctd_type, wt):
        self.is_changed_type(locators.TYPE_INPUT, xpctd_type, wt)

    def should_not_be_changed_status_time(self, xpctd_text, wt):
        text = self.driver.find_by_css(locators.COMPLETE_AVERAGE_TIME_CELL, wt).text
        assert text == xpctd_text, 'Status time is "{}", but expected "{}"'.format(text, xpctd_text)

    def should_be_changed_status_time(self, xpctd_text, wt):
        text = self.driver.find_by_css(locators.SCREENOUT_AVERAGE_TIME_CELL, wt).text
        assert text == xpctd_text, 'Status time is "{}", but expected "{}"'.format(text, xpctd_text)

    def should_be_changed_manager_name(self, dflt_manager, xpctd_manager, wt):
        self.is_changed_dropdown(locators.MANAGER_INPUT, dflt_manager, xpctd_manager, wt)

    def should_be_changed_project_manager_name(self, dflt_prj_manager, xpctd_prj_manager, wt):
        self.is_changed_dropdown(locators.PROJECT_MANAGER_INPUT, dflt_prj_manager, xpctd_prj_manager, wt)

    def should_be_changed_url_template(self, xpctd_url, wt):
        self.is_changed_input(locators.URL_TEMPLATE_INPUT, xpctd_url, wt)

    def should_be_changed_inner_name(self, xpctd_inner_name, wt):
        self.is_changed_input(locators.INNER_NAME_INPUT, xpctd_inner_name, wt)

    def should_be_changed_name(self, xpctd_name, wt):
        self.is_changed_input(locators.NAME_INPUT, xpctd_name, wt)

    def should_be_changed_sync(self, wt):
        self.is_changed_toggle(locators.SYNC_TOGGLE, wt)

    def should_be_changed_description(self, xpctd_text, wt):
        self.is_changed_input(locators.DESCRIPTION_INPUT, xpctd_text, wt)

    def should_be_changed_comments(self, xpctd_text, wt):
        self.is_changed_input(locators.COMMENTS_INPUT, xpctd_text, wt)

    def should_be_changed_device_type(self, dflt_type, xpctd_type, wt):
        self.is_changed_dropdown(locators.DEVICE_TYPE_INPUT, dflt_type, xpctd_type, wt)

    def should_be_changed_device_type_show(self, dflt_type, xpctd_type, wt):
        self.is_changed_dropdown(locators.DEVICE_TYPE_SHOW_INPUT, dflt_type, xpctd_type, wt)

    def should_be_changed_multilink(self, wt):
        self.is_changed_toggle(locators.MULTILINKS_TOGGLE, wt)

    def should_be_collector_template_url(self):
        time.sleep(1)
        assert '/collectortemplates/' in self.driver.url, 'Should be collector template url, but not'

    def save_project_changes(self):
        self.driver.find_by_text('Сохранить').first.click()

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

    def add_collector_template(self, tmplt_name, wt):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        self.driver.find_by_css(locators.ADD_COLLECTOR_TEMPLATE_BUTTON).first.click()
        self.driver.find_by_css(locators.COLLECTOR_TEMPLATE_NAME_INPUT).type(tmplt_name)
        self.driver.find_by_css(locators.COLLECTOR_TEMPLATE_NAME_CONFIRM_BUTTON).click()
