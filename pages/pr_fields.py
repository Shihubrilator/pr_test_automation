import time


def set_dropdown(driver, input_locator, list_item_locator, li_number, wait_time):
    driver.find_by_css(input_locator, wait_time).first.click()
    time.sleep(0.5)
    driver.find_by_css(list_item_locator, wait_time)[li_number].click()


def set_input(driver, input_locator, value, wait_time):
    driver.find_by_css(input_locator, wait_time)[0].clear()
    driver.find_by_css(input_locator, wait_time)[0].fill(value)


def set_toggle(driver, toggle_locator, wait_time):
    if driver.is_element_present_by_css(toggle_locator, wait_time):
        driver.find_by_css(toggle_locator, wait_time).click()


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
    assert not driver.is_element_present_by_css(dropdown_locator + ' input[value="' + default_text + '"]',
                                                wait_time), 'Dropdown is not changed'
    assert driver.is_element_present_by_css(dropdown_locator + ' input[value="' + xpctd_text + '"]',
                                            wait_time), 'Dropdown is not found'


def is_changed_input(driver, xpctd_text):
    assert driver.is_element_present_by_value(xpctd_text), 'Input with text "' + xpctd_text + '" is not found'


def is_changed_toggle(driver, toggle_locator, wait_time):
    assert driver.is_element_present_by_css(toggle_locator + '--checked', wait_time), \
        'Element "' + toggle_locator + '--checked" is not found'


def is_changed_type(driver, xpctd_type, wait_time):
    assert driver.is_element_present_by_text(xpctd_type, wait_time), 'Type is not changed'


def is_changed_category(driver, selected_category_locator, xpctd_category, wait_time):
    category = driver.find_by_css(selected_category_locator, wait_time).text
    xpctd_category += ' ×'
    assert category == xpctd_category, 'Category "' + category + '" expected to be "' + xpctd_category + '"'
