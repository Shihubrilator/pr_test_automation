from pages.login_page import LoginPage


def test_login(browser, config):
    #login = config['login']
    #passwd = config['passwd']
    url = 'http://qa.panelrider.com/'#config['url']
    page = LoginPage(driver=browser, base_url=url)
    page.open()
