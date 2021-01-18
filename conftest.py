import pytest
from splinter import Browser
import yaml
import requests
import json


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = Browser("chrome")
        browser.driver.set_window_size(1900, 1000)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = Browser("firefox")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


def get_config():
    with open("config.yml", "r", encoding='utf8') as ymlfile:
        return yaml.load(ymlfile, Loader=yaml.FullLoader)


@pytest.fixture(scope='session')
def config():
    return get_config()


@pytest.fixture(scope='session')
def login(config):
    """получение куки авторизации"""
    request_url = config['pr']['url'] + 'api/v2/admin/panel/0/login'
    payload = json.dumps({'Email': config['pr']['login'], 'Password': config['pr']['passwd']})
    headers = {'Accept': config['pr']['headers']['accept'],
               'Content-Type': config['pr']['headers']['content_type']}
    r = requests.post(url=request_url, data=payload, headers=headers)
    return r.cookies.get_dict()['authtoken']


@pytest.fixture()
def pr_headers(login, config):
    """лепим хидер запроса"""
    return {'Accept': 'application/json',
            'Cookie': 'authtoken=' + login,
            'Content-Type': 'application/json'}
