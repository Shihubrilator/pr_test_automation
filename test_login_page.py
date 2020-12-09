from pages.login_page import LoginPage
from pages.projects_list_page import ProjectsListPage
import time


def test_login(browser, config):
    login = config['pr']['login']
    passwd = config['pr']['passwd']
    url = config['pr']['url']
    page = LoginPage(driver=browser, base_url=url)
    page.open()
    page.login(login, passwd)
    projects_page = ProjectsListPage(driver=browser)
    projects_page.should_be_projects_url()
