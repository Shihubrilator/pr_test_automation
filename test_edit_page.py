from pages.login_page import LoginPage
from pages.edit_page import EditPage
import time


def test_change_project_settings(browser, config):
    login = config['pr']['login']
    passwd = config['pr']['passwd']
    url = config['pr']['url']
    #логин через api и подсовывание куки в драйвер
    login_page = LoginPage(driver=browser, base_url=url)
    login_page.open()
    login_page.login(login, passwd)
    time.sleep(1)
    url = 'http://qa.panelrider.com/admin/projects/765277185'
    page = EditPage(driver=browser, base_url=url)
    page.open()
    time.sleep(1)
    page.set_manager()
    page.set_project_manager()
    time.sleep(5)
