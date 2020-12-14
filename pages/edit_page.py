from pypom import Page
import time


class EditPage(Page):
    def set_manager(self):
        manager_option = self.driver.find_by_class('.form-group')[2]
        manager_option.find_by_css_selector('div[role="combobox"]').click()
        time.sleep(1)
        manager_option.find_by_css_selector('li.rw-list-option:last-of-type').click()
        time.sleep(1)

    def set_project_manager(self):
        pass
