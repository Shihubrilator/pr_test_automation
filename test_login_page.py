from pages.login_page import LoginPage
from pages.projects_list_page import ProjectsListPage


def test_login(browser, config):
    page = LoginPage(driver=browser, base_url=config['pr']['url'])
    page.open()
    page.login(config['pr']['login'], config['pr']['passwd'])
    projects_page = ProjectsListPage(driver=browser)
    projects_page.should_be_projects_url()
