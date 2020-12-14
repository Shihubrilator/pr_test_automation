from pages.login_page import LoginPage
from pages.edit_page import EditPage
import time


def test_change_project_settings(browser, config):
    login = config['pr']['login']
    passwd = config['pr']['passwd']
    url = config['pr']['url']
    login_page = LoginPage(driver=browser, base_url=url)
    login_page.open()
    login_page.login(login, passwd)
    time.sleep(5)
    url = 'http://qa.panelrider.com/admin/projects/217217531'
    page = EditPage(driver=browser, base_url=url)
    page.open()
    time.sleep(10)
    page.set_project_manager()
    time.sleep(5)
