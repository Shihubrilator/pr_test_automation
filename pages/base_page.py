from pypom import Page
import time
from selenium.webdriver.common.keys import Keys


class BasePage(Page):
    @staticmethod
    def clear_text_input(input_object):
        while len(input_object.value) > 0:
            input_object.type(Keys.BACKSPACE)

    @staticmethod
    def async_wait(my_async_ops, locator):
        _ = True
        while _:
            try:
                text = my_async_ops(locator).text
            except Exception as exc:
                pass
                #print('Func not ready, waiting...')
            else:
                if len(text) > 0:
                    _ = False

    def set_dropdown(self, input_locator, list_item_locator, li_number, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        self.driver.find_by_css(input_locator).first.click()
        time.sleep(0.5)
        self.driver.find_by_css(list_item_locator)[li_number].click()

    def set_input(self, input_locator, value, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        input_object = self.driver.find_by_css(input_locator).first
        self.clear_text_input(input_object)
        input_object.fill(value)

    def set_toggle(self, locator, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        self.driver.find_by_css(locator).click()

    def set_checkbox(self, locator, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        self.driver.find_by_css(locator).click()

    def set_type(self, type_input_locator, type_list_item_locator, type_list_item_locator_num, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        self.driver.find_by_css(type_input_locator).first.click()
        time.sleep(0.5)
        self.driver.find_by_css(type_list_item_locator)[type_list_item_locator_num].click()

    def set_category(self, category_list_locator, category_list_item_locator, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        self.driver.find_by_css(category_list_locator).click()
        time.sleep(0.5)
        self.driver.find_by_css(category_list_item_locator)[3].click()

    def is_changed_dropdown(self, dropdown_locator, default_text, xpctd_text, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        assert not self.driver.is_element_present_by_css('{} input[value="{}"]'.format(dropdown_locator, default_text)),\
                                                         'Dropdown value "{}" was found'.format(default_text)
        assert self.driver.is_element_present_by_css('{} input[value="{}"]'.format(dropdown_locator, xpctd_text)), \
                                                     'Dropdown value is "{}" was not found'.format(xpctd_text)

    def is_changed_input(self, input_locator, xpctd_text, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        field_text = self.driver.find_by_css(input_locator).first.value
        assert field_text == xpctd_text, 'Input value is "{}" while expected "{}"'.format(field_text, xpctd_text)

    def is_changed_toggle(self, toggle_locator, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        assert self.driver.is_element_present_by_css(toggle_locator + '--checked'), \
            'Element "{} --checked" is not found'.format(toggle_locator)

    def is_changed_type(self, type_locator, xpctd_type, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        el_type = self.driver.find_by_css(type_locator).text
        assert el_type == xpctd_type, 'Type is "{}" while expected "{}"'.format(el_type, xpctd_type)

    def is_changed_category(self, selected_category_locator, xpctd_category, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        category = self.driver.find_by_css(selected_category_locator).text[0:-2]
        assert category == xpctd_category, 'Category "{}" expected to be "{}"'.format(category, xpctd_category)

    def is_changed_checkbox(self, locator, wait_time):
        self.async_wait(self.driver.find_by_css, 'h3 a')
        assert self.driver.find_by_css(locator + ' input').first.checked, "Not checked"
