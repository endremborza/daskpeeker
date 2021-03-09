import pytest
from selenium.webdriver import Chrome

from daskpeeker.tests.peeker_for_testing import PeekerRunner


@pytest.fixture(scope="session")
def browser(request):
    pr = PeekerRunner()
    pr.start()
    request.addfinalizer(pr.stop)

    browser = Chrome()
    browser.maximize_window()
    request.addfinalizer(browser.close)
    return browser
