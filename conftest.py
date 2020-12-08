import pytest
from splinter import Browser
import yaml


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
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = browser = Browser("firefox")
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
