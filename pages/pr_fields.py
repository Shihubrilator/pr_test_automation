import time
from selenium.webdriver.common.keys import Keys


def set_dropdown(driver, input_locator, list_item_locator, li_number, wait_time):
    driver.find_by_css(input_locator, wait_time).first.click()
    time.sleep(0.5)
    driver.find_by_css(list_item_locator, wait_time)[li_number].click()


def set_input(driver, input_locator, value, wait_time):
    while len(driver.find_by_css(input_locator, wait_time).first.value) > 0:
        driver.find_by_css(input_locator, wait_time).first.type(Keys.BACKSPACE)
    driver.find_by_css(input_locator, wait_time).first.fill(value)


def set_toggle(driver, locator, wait_time):
    driver.find_by_css(locator, wait_time).click()


def set_checkbox(driver, locator, wait_time):
    driver.find_by_css(locator, wait_time).click()


def set_type(driver, type_input_locator, type_list_item_locator, type_list_item_locator_num, wait_time):
    if driver.is_element_present_by_css(type_input_locator, wait_time):
        driver.find_by_css(type_input_locator)[0].click()
    driver.find_by_css(type_list_item_locator)[type_list_item_locator_num].click()


def set_category(driver, category_list_locator, category_list_item_locator, wait_time):
    if driver.is_element_present_by_css(category_list_locator, wait_time):
        driver.find_by_css(category_list_locator).click()
    if driver.is_element_present_by_css(category_list_item_locator, wait_time):
        time.sleep(0.5)
        driver.find_by_css(category_list_item_locator)[3].click()


def is_changed_dropdown(driver, dropdown_locator, default_text, xpctd_text, wait_time):
    assert not driver.is_element_present_by_css(dropdown_locator + ' input[value="' + default_text + '"]', wait_time), \
        'Dropdown value "{}" was found'.format(default_text)
    assert driver.is_element_present_by_css(dropdown_locator + ' input[value="' + xpctd_text + '"]', wait_time), \
        'Dropdown value is "{}" was not found'.format(xpctd_text)


def is_changed_input(driver, input_locator, xpctd_text, wait_time):
    time.sleep(2)
    field_text = driver.find_by_css(input_locator, wait_time).first.value
    assert field_text == xpctd_text, 'Input value is "{}" while expected "{}"'.format(field_text, xpctd_text)


def is_changed_toggle(driver, toggle_locator, wait_time):
    assert driver.is_element_present_by_css(toggle_locator + '--checked', wait_time), \
        'Element "{} --checked" is not found'.format(toggle_locator)


def is_changed_type(driver, xpctd_type, wait_time):
    assert driver.is_element_present_by_text(xpctd_type, wait_time), 'Type is not changed'


def is_changed_category(driver, selected_category_locator, xpctd_category, wait_time):
    category = driver.find_by_css(selected_category_locator, wait_time).text
    xpctd_category += ' ×'
    assert category == xpctd_category, 'Category "{}" expected to be "{}"'.format(category, xpctd_category)


def is_changed_checkbox(driver, locator, wait_time):
    time.sleep(2)
    assert driver.find_by_css(locator + ' input', wait_time)[0].checked, "Not checked"
