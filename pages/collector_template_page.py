import time
import requests
from .base_page import BasePage
from .locators import CollectorTemplatePageLocators as locators
import json


class CollectorTemplatePage(BasePage):
    def change_name(self, xpctd_name, wt):
        self.set_input(locators.TEMPLATE_NAME_INPUT, xpctd_name, wt)

    def change_panel(self, li_num, wt):
        self.set_dropdown(locators.TEMPLATE_PANEL, locators.TEMPLATE_PANEL_LIST_ITEM, li_num, wt)

    def change_invitation(self, li_num, wt):
        self.set_dropdown(locators.TEMPLATE_INVITATION, locators.TEMPLATE_INVITATION_LIST_ITEM, li_num, wt)

    def change_reminder(self, li_num, wt):
        self.set_dropdown(locators.TEMPLATE_REMINDER, locators.TEMPLATE_REMINDER_LIST_ITEM, li_num, wt)

    def change_autofill(self, li_num, wt):
        self.set_dropdown(locators.TEMPLATE_AUTOFILL, locators.TEMPLATE_AUTOFILL_LIST_ITEM, li_num, wt)

    def change_captcha(self, li_num, wt):
        self.set_dropdown(locators.TEMPLATE_CAPTCHA, locators.TEMPLATE_CAPTCHA_LIST_ITEM, li_num, wt)

    def change_allowduplicate(self, wt):
        self.set_checkbox(locators.TEMPLATE_ALLOWDUPLICATES, wt)

    def change_reward(self, xpctd_reward, wt):
        self.set_input(locators.TEMPLATE_REWARD, xpctd_reward, wt)

    def should_be_changed_name(self, xpctd_name, wt):
        self.is_changed_input(locators.TEMPLATE_NAME_INPUT, xpctd_name, wt)

    def should_be_changed_panel(self, dflt_panel, xpctd_panel, wt):
        self.is_changed_dropdown(locators.TEMPLATE_PANEL, dflt_panel, xpctd_panel, wt)

    def should_be_changed_invitation(self, dflt_invitation, xpctd_invitation, wt):
        self.is_changed_dropdown(locators.TEMPLATE_INVITATION, dflt_invitation, xpctd_invitation, wt)

    def should_be_changed_reminder(self, dflt_reminder, xpctd_reminder, wt):
        self.is_changed_dropdown(locators.TEMPLATE_REMINDER, dflt_reminder, xpctd_reminder, wt)

    def should_be_changed_autofill(self, dflt_autofill, xpctd_autofill, wt):
        self.is_changed_dropdown(locators.TEMPLATE_AUTOFILL, dflt_autofill, xpctd_autofill, wt)

    def should_be_changed_captcha(self, dflt_captcha, xpctd_captcha, wt):
        time.sleep(2)
        self.is_changed_dropdown(locators.TEMPLATE_CAPTCHA, dflt_captcha, xpctd_captcha, wt)

    def should_be_changed_allowduplicates(self, wt):
        self.is_changed_checkbox(locators.TEMPLATE_ALLOWDUPLICATES, wt)

    def should_be_changed_reward(self, xpctd_reward, wt):
        self.is_changed_input(locators.TEMPLATE_REWARD, '{}.00'.format(xpctd_reward), wt)

    def save_changes(self):
        self.driver.find_by_text('Сохранить').first.click()

    def reload(self):
        self.driver.reload()

    @staticmethod
    def set_default_c_template_settings(headers, config):
        request_url = config['pr']['url'] + \
                      'api/v2/admin/panel/0/collectortemplates/' + str(config['pr']['c_template_id'])
        data = json.dumps(config['pr']['default_c_template_settings_json'])
        requests.patch(url=request_url, headers=headers, data=data)
