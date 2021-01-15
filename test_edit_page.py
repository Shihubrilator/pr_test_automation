from pages.login_page import LoginPage
from pages.edit_page import EditPage


def test_change_project_settings(browser, config):
    url = config['pr']['project_url']
    login_page = LoginPage(driver=browser, base_url=url)
    login_page.open()
    login_page.login(config['pr']['login'], config['pr']['passwd'])
    page = EditPage(driver=browser, base_url=url)
    page.set_managers()
    page.save_project_changes()
    page.reload()
    page.should_be_changed_managers_name()
