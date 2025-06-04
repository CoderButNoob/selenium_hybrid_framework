import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # yield driver
    # driver.quit()
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Lauching chrome")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox")
    return driver



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
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


