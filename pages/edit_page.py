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

    def set_manager(self):
        if self.driver.is_element_present_by_css(locators.MANAGER_INPUT, self.wait_time):
            self.driver.find_by_css(locators.MANAGER_INPUT).first.click()
        if self.driver.is_element_present_by_css(locators.MANAGER_LIST_ITEM, self.wait_time):
            time.sleep(0.5)
            self.driver.find_by_css(locators.MANAGER_LIST_ITEM)[4].click()

    def set_project_manager(self):
        if self.driver.is_element_present_by_css(locators.PROJECT_MANAGER_INPUT, self.wait_time):
            self.driver.find_by_css(locators.PROJECT_MANAGER_INPUT).first.click()
        if self.driver.is_element_present_by_css(locators.PROJECT_MANAGER_LIST_ITEM, self.wait_time):
            time.sleep(0.5)
            self.driver.find_by_css(locators.PROJECT_MANAGER_LIST_ITEM)[4].click()

    def set_template_url(self, changed_url):
        if self.driver.is_element_present_by_name(locators.URL_TEMPLATE_INPUT, self.wait_time):
            self.driver.find_by_name(locators.URL_TEMPLATE_INPUT)[0].fill(changed_url)

    def set_inner_name(self):
        if self.driver.is_element_present_by_name(locators.INNER_NAME_INPUT, self.wait_time):
            self.driver.find_by_name(locators.INNER_NAME_INPUT)[0].fill(self.inner_name)

    def set_name(self):
        if self.driver.is_element_present_by_name(locators.NAME_INPUT, self.wait_time):
            self.driver.find_by_name(locators.NAME_INPUT)[0].fill(self.name)

    def set_type(self):
        if self.driver.is_element_present_by_css(locators.TYPE_INPUT, self.wait_time):
            self.driver.find_by_css(locators.TYPE_INPUT)[0].click()
        self.driver.find_by_css(locators.TYPE_LIST_ITEM)[2].click()

    def set_sync(self):
        if self.driver.is_element_present_by_css('.form-group:nth-child(7) .react-toggle', self.wait_time):
            self.driver.find_by_css('.form-group:nth-child(7) .react-toggle').click()

    def set_description(self):
        if self.driver.is_element_present_by_name(locators.DESCRIPTION_INPUT):
            self.driver.find_by_name(locators.DESCRIPTION_INPUT).fill(self.description)

    def set_comments(self):
        if self.driver.is_element_present_by_name(locators.COMMENTS_INPUT):
            self.driver.find_by_name(locators.COMMENTS_INPUT).fill(self.note)

    def save_project_changes(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_by_text('Сохранить')[0].click()

    def reload(self):
        self.driver.reload()

    def should_be_changed_manager_name(self):
        assert not self.driver.find_by_css(locators.MANAGER_INPUT + ' input[value="Админ"]', 5)
        #брать имя менеджера из базы
        assert self.driver.find_by_css(locators.MANAGER_INPUT + ' input[value="Бот"]', 5), \
            'manager name should be Бот, but not'

    def should_be_changed_project_manager_name(self):
        assert self.driver.find_by_css(locators.PROJECT_MANAGER_INPUT + ' input[value="Бот"]', 5), \
            'project manager name should be Бот, but not'

    def should_be_changed_url_template(self, changed_url):
        url_template = self.driver.find_by_name(locators.URL_TEMPLATE_INPUT).text
        assert url_template == changed_url, 'url template expected to be equal to ' + changed_url + ', but not'

    def should_be_changed_inner_name(self):
        inner_name_value = self.driver.find_by_name(locators.INNER_NAME_INPUT)[0].value
        assert inner_name_value == self.inner_name, 'project InnerName expected to be equal to ' \
                                                    + self.inner_name + 'but not'

    def should_be_changed_name(self):
        name_value = self.driver.find_by_name(locators.NAME_INPUT)[0].value
        assert name_value == self.name, 'project Name expected to be equal to ' + self.name + ', but not'

    def should_be_changed_type(self):
        selected_type = self.driver.find_by_css(locators.TYPE_INPUT).text
        assert selected_type == self.xpctd_type, 'type expected to be ' + self.xpctd_type + ', but not'

    def should_be_changed_sync(self):
        assert self.driver.is_element_present_by_css('.form-group:nth-child(7) .react-toggle--checked', self.wait_time)

    def should_be_changed_description(self):
        description_text = self.driver.find_by_name(locators.DESCRIPTION_INPUT).text
        assert description_text == self.description, 'project description expected to be equal to ' + self.description \
                                                     + ', but not'

    def should_be_changed_comments(self):
        comment_text = self.driver.find_by_name(locators.COMMENTS_INPUT).text
        assert comment_text == self.note, 'project description expected to be equal to ' + self.note + ', but not'

    @staticmethod
    def set_default_settings(headers, config):
        request_url = config['pr']['url'] + 'api/v2/admin/panel/0/survey/' + str(config['pr']['project_id'])
        payload = json.dumps(config['pr']['default_project_settings'])
        requests.put(url=request_url, headers=headers, data=payload)
        # проверить, что запрос отправился
