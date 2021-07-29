import time

import requests
from pypom import Page
from .locators import CollectorTemplatePageLocators as locators
from .pr_fields import set_input, set_dropdown, is_changed_input, is_changed_dropdown, set_checkbox, is_changed_checkbox
import json


class CollectorTemplatePage(Page):
    def change_name(self, config):
        set_input(self.driver, locators.TEMPLATE_NAME_INPUT,
                  config['pr']['xpctd_c_tmplt_settings']['name'], config['pr']['wait_time'])

    def change_panel(self, config):
        set_dropdown(self.driver, locators.TEMPLATE_PANEL,
                     locators.TEMPLATE_PANEL_LIST_ITEM, 4, config['pr']['wait_time'])

    def change_invitation(self, config):
        set_dropdown(self.driver, locators.TEMPLATE_INVITATION,
                     locators.TEMPLATE_INVITATION_LIST_ITEM, 1, config['pr']['wait_time'])

    def change_reminder(self, config):
        set_dropdown(self.driver, locators.TEMPLATE_REMINDER,
                     locators.TEMPLATE_REMINDER_LIST_ITEM, 1, config['pr']['wait_time'])

    def change_autofill(self, config):
        set_dropdown(self.driver, locators.TEMPLATE_AUTOFILL,
                     locators.TEMPLATE_AUTOFILL_LIST_ITEM, 1, config['pr']['wait_time'])

    def change_captcha(self, config):
        set_dropdown(self.driver, locators.TEMPLATE_CAPTCHA,
                     locators.TEMPLATE_CAPTCHA_LIST_ITEM, 1, config['pr']['wait_time'])

    def change_allowduplicate(self, config):
        set_checkbox(self.driver, locators.TEMPLATE_ALLOWDUPLICATES, config['pr']['wait_time'])

    def change_reward(self, config):
        set_input(self.driver, locators.TEMPLATE_REWARD, '40', config['pr']['wait_time'])

    def should_be_changed_name(self, config):
        is_changed_input(self.driver, locators.TEMPLATE_NAME_INPUT,
                         config['pr']['xpctd_c_tmplt_settings']['name'], config['pr']['wait_time'])

    def should_be_changed_panel(self, config):
        is_changed_dropdown(self.driver, locators.TEMPLATE_PANEL,
                            config['pr']['default_c_template_settings']['panel'],
                            config['pr']['xpctd_c_tmplt_settings']['panel'], config['pr']['wait_time'])

    def should_be_changed_invitation(self, config):
        is_changed_dropdown(self.driver, locators.TEMPLATE_INVITATION,
                            config['pr']['default_c_template_settings']['invitation'],
                            config['pr']['xpctd_c_tmplt_settings']['invitation'], config['pr']['wait_time'])

    def should_be_changed_reminder(self, config):
        is_changed_dropdown(self.driver, locators.TEMPLATE_REMINDER,
                            config['pr']['default_c_template_settings']['reminder'],
                            config['pr']['xpctd_c_tmplt_settings']['reminder'], config['pr']['wait_time'])

    def should_be_changed_autofill(self, config):
        is_changed_dropdown(self.driver, locators.TEMPLATE_AUTOFILL,
                            config['pr']['default_c_template_settings']['autofill'],
                            config['pr']['xpctd_c_tmplt_settings']['autofill'], config['pr']['wait_time'])

    def should_be_changed_captcha(self, config):
        time.sleep(2)
        is_changed_dropdown(self.driver, locators.TEMPLATE_CAPTCHA,
                            config['pr']['default_c_template_settings']['captcha'],
                            config['pr']['xpctd_c_tmplt_settings']['captcha'], config['pr']['wait_time'])

    def should_be_changed_allowduplicates(self, config):
        is_changed_checkbox(self.driver, locators.TEMPLATE_ALLOWDUPLICATES, config['pr']['wait_time'])

    def should_be_changed_reward(self, config):
        is_changed_input(self.driver, locators.TEMPLATE_REWARD, '40.00', config['pr']['wait_time'])

    def save_changes(self):
        self.driver.find_by_text('Сохранить')[0].click()

    def reload(self):
        self.driver.reload()

    @staticmethod
    def set_default_c_template_settings(headers, config):
        request_url = config['pr']['url'] + \
                      'api/v2/admin/panel/0/collectortemplates/' + str(config['pr']['c_template_id'])
        data = json.dumps(config['pr']['default_c_template_settings_json'])
        requests.patch(url=request_url, headers=headers, data=data)
