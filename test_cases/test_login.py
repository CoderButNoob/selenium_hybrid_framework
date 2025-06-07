import pytest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_login:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger =  LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("************************* Test_001_login **********************")
        self.logger.info("************************* Verify Homepage Title **********************")

        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        screenshot_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshot')
        os.makedirs(screenshot_dir, exist_ok=True)

        if actual_title == "OrangeHRM":
            assert True
            self.driver.close()
            self.logger.info("************************* HomePage Title Test passed **********************")

        else:
            self.driver.save_screenshot(os.path.join(screenshot_dir, 'test_homePageTitle.png'))
            self.driver.close()
            self.logger.info("************************* HomePage Title Test failed **********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************************* Verifying Login Test **********************")

        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        WebDriverWait(self.driver, 10).until(EC.title_contains("OrangeHRM"))
        actual_title = self.driver.title
        print("Actual title after login:", actual_title)

        screenshot_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshot')
        os.makedirs(screenshot_dir, exist_ok=True)

        if actual_title == "OrangeHRM":
            assert True
            self.logger.info("************************* Login Test passed **********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.join(screenshot_dir, 'test_login.png'))
            self.logger.info("************************* Login Test fails **********************")
            self.driver.close()
            assert False
