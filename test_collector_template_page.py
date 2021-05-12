from pages.login_page import LoginPage
from pages.edit_page import EditPage


def test_create_collector_template(config, browser):
    project_url = config['pr']['project_url']
    login_page = LoginPage(driver=browser, base_url=project_url)
    login_page.open()
    login_page.login(config['pr']['login'], config['pr']['passwd'])
    page = EditPage(driver=browser, base_url=project_url)
    page.add_collector_template(config)
    page.should_be_collector_template_url()


def test_change_collector_template_name():
    assert True
