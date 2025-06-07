import pytest
from selenium import webdriver
import sys
import os

# Add the project root (orangeHRM) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="function")
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()



def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#################### PyTest HTML Report #######################

#It is Hook for adding environment info to HTML Report
def pytest_configure(config):
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'orangeHRM'
        config._metadata['Module Name'] = 'customers'
        config._metadata['Tester'] = 'Aniket'


#this is the Hook to delete/modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


