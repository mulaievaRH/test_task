from lib2to3.pgen2 import driver
import pytest
from  selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service as chr_s
from selenium.webdriver.firefox.service import Service as ff_s
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# chrome_service = chr_s(ChromeDriverManager().install())

# Chrome=wd.Chrome(service=chrome_service)
# Firefox=wd.Firefox(service=ff_service)


# @pytest.fixture()
# def setup(request):
#     browsers = [Chrome,Firefox]
#     import pdb; pdb.set_trace()
#     for driver in browsers:
#         driver.get("https://staging.scrive.com/t/9221714692410699950/7348c782641060a9")
#         driver.maximize_window()
#         yield
#         driver.close()    
        
@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == "chrome":
        service = chr_s(ChromeDriverManager().install())
        driver = wd.Chrome(service=service)
    elif browser == "ff":
        service = ff_s(GeckoDriverManager().install())
        driver = wd.Firefox(service=service)
    else:
        print ("provide a browser")
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


