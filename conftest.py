import pytest
from splinter import Browser
import yaml
import requests
import json
from pages.login_page import LoginPage
from pages.edit_page import EditPage
import time
from datetime import datetime
import pathlib


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="module")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = Browser("chrome")#, headless=True)
        browser.driver.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = Browser("firefox")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\n\nquit browser..")
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


@pytest.fixture(scope='module')
def pr_headers(login, config):
    """лепим хидер запроса"""
    return {'Accept': 'application/json',
            'Cookie': 'authtoken=' + login,
            'Content-Type': 'application/json'}

@pytest.fixture(scope='module')
def pr_edit_page(browser, config, pr_headers):
    url = config['pr']['project_url']
    login_page = LoginPage(driver=browser, base_url=url)
    login_page.open()
    login_page.login(config['pr']['login'], config['pr']['passwd'])
    page = EditPage(driver=browser, base_url=url)
    page.change_settings(config)
    page.save_project_changes()
    page.reload()
    page.change_status_time_and_cancel(config)
    page.change_status_time(config)
    yield page
    page.set_default_settings(pr_headers, config)

# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)

# check if a test has failed
@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            driver = request.node.funcargs['browser']
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)

# make a screenshot with a name of the test, date and time
def take_screenshot(driver, nodeid):
    time.sleep(1)
    file_name = f'{nodeid}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}'\
        .replace("/", "_").replace(":", "_").replace(".", "_")
    driver.screenshot(str(pathlib.Path().absolute()) + '/Screenshots/' + file_name)
