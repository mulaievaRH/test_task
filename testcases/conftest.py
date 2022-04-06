import pytest
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service as chr_s
from selenium.webdriver.firefox.service import Service as ff_s
from selenium.webdriver.ie.service import Service as ie_s
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == "chrome":
        service = chr_s(ChromeDriverManager().install())
        driver = wd.Chrome(service=service)
    elif browser == "ff":
        service = ff_s(GeckoDriverManager().install())
        driver = wd.Firefox(service=service)
    elif browser == "IE":
        service = ie_s(IEDriverManager().install())
        driver = wd.Ie(service=service)
    else:
        print("provide a browser")
    driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
