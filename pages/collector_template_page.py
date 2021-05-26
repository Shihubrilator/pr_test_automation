import requests
from pypom import Page
from .locators import CollectorTemplatePageLocators as locators
from .pr_fields import set_input, set_dropdown, is_changed_input, is_changed_dropdown
import json


class CollectorTemplatePage(Page):
    def change_name(self, config):
        set_input(self.driver, locators.TEMPLATE_NAME_INPUT,
                  config['pr']['xpctd_c_tmplt_settings']['name'], config['pr']['wait_time'])

    def change_panel(self, config):
        set_dropdown(self.driver, locators.TEMPLATE_PANEL,
                     locators.TEMPLATE_PANEL_LIST_ITEM, 4, config['pr']['wait_time'])

    def should_be_changed_name(self, config):
        is_changed_input(self.driver, config['pr']['xpctd_c_tmplt_settings']['name'])

    def should_be_changed_panel(self, config):
        is_changed_dropdown(self.driver, locators.TEMPLATE_PANEL,
                            config['pr']['default_c_template_settings']['panel'],
                            config['pr']['xpctd_c_tmplt_settings']['panel'], config['pr']['wait_time'])

    def save_changes(self):
        self.driver.find_by_text('Сохранить')[0].click()

    def reload(self):
        self.driver.reload()

    @staticmethod
    def set_default_c_template_settings(headers, config):
        request_url = config['pr']['url'] + \
                      'api/v2/admin/panel/0/collectortemplates/' + str(config['pr']['c_template_id'])
        data = json.dumps(config['pr']['default_c_template_settings_json'])
        r = requests.patch(url=request_url, headers=headers, data=data)
