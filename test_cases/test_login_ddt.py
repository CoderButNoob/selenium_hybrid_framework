# import time
# import pytest
# import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from page_objects.login_page import LoginPage
# from page_objects.home_page import HomePage
# from utilities.read_properties import ReadConfig
# from utilities.customLogger import LogGen
# from utilities import xlutils
#
# class Test_002_DDT_login:
#     base_url = ReadConfig.getApplicationUrl()
#     path = os.path.join(os.path.dirname(__file__), '..', 'test_data', 'login_data.xlsx')
#     logger =  LogGen.loggen()
#
#     def test_login_ddt(self, setup):
#         self.logger.info("************************* Test_002_DDT_login ************************")
#         self.logger.info("************************* Verifying Login DDT Test **********************")
#
#         self.driver = setup
#         self.driver.get(self.base_url)
#         self.lp = LoginPage(self.driver)
#         self.hp = HomePage(self.driver)
#
#         self.rows = xlutils.getRowCount(self.path,'Sheet1')
#         print("Number of rows in excel: ",self.rows)
#
#         list_status = []
#
#         for r in range(2,self.rows+1):
#             self.user = xlutils.readData(self.path,'Sheet1',r,1)
#             self.password = xlutils.readData(self.path,'Sheet1',r,2)
#             self.exp = xlutils.readData(self.path,'Sheet1',r,3)
#
#             self.logger.info(f"Test Row: {r} | Username: {self.user} | Expected: {self.exp}")
#
#             self.driver.get(self.base_url)  # Reload for each test iteration
#
#             # Wait for login field to appear
#             try:
#                 WebDriverWait(self.driver, 15).until(
#                     EC.presence_of_element_located((By.NAME, "username"))
#                 )
#             except:
#                 self.logger.error("Login page did not load properly.")
#                 list_status.append("Fail")
#                 continue
#
#             try:
#                 self.lp.setUserName(self.user)
#                 self.lp.setPassword(self.password)
#                 self.lp.clickLogin()
#             except Exception as e:
#                 self.logger.error(f"Exception during login: {str(e)}")
#                 list_status.append("Fail")
#                 continue
#
#             # self.lp.setUserName(self.user)
#             # self.lp.setPassword(self.password)
#             # self.lp.clickLogin()
#             # time.sleep(5)
#
#             act_title = self.driver.title
#             exp_title = "OrangeHRM"
#
#             if  act_title == exp_title:
#                 if self.exp == 'pass':
#                     self.logger.info("*** Passed ***")
#                     list_status.append("Pass")
#                     self.hp.logout()
#                 elif self.exp == "fail":
#                     self.logger.info("*** Failed ***")
#                     list_status.append("Fail")
#             elif  act_title != exp_title:
#                 if self.exp == 'pass':
#                     self.logger.info("*** Failed ***")
#                     list_status.append("Fail")
#                 elif self.exp == "fail":
#                     self.logger.info("*** Passed ***")
#                     list_status.append("Pass")
#
#
#
#         if "Fail" not in list_status:
#             self.logger.info("Login DDT passed ....")
#             self.driver.close()
#             assert True
#         else:
#             self.logger.info("Login DDT failed ....")
#             self.driver.close()
#             assert False
#
#         self.logger.info("********** END of login DDT Test ************")
#         self.logger.info("************* Completed Test_002_DDT_login **************")
#
#
#
#
#
#
#         # self.lp.setUserName(self.username)
#         # self.lp.setPassword(self.password)
#         # self.lp.clickLogin()
#         #
#         # WebDriverWait(self.driver, 10).until(EC.title_contains("OrangeHRM"))
#         # actual_title = self.driver.title
#         # print("Actual title after login:", actual_title)
#         #
#         # screenshot_dir = os.path.join(os.path.dirname(__file__), '..', 'screenshot')
#         # os.makedirs(screenshot_dir, exist_ok=True)
#         #
#         # if actual_title == "OrangeHRM":
#         #     assert True
#         #     self.logger.info("************************* Login Test passed **********************")
#         #     self.driver.close()
#         # else:
#         #     self.driver.save_screenshot(os.path.join(screenshot_dir, 'test_login.png'))
#         #     self.logger.info("************************* Login Test fails **********************")
#         #     self.driver.close()
#         #     assert False
import time
import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlutils

class Test_002_DDT_login:
    base_url = ReadConfig.getApplicationUrl()
    path = os.path.join(os.path.dirname(__file__), '..', 'test_data', 'login_data.xlsx')
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************************* Test_002_DDT_login ************************")
        self.logger.info("************************* Verifying Login DDT Test **********************")

        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)

        self.rows = xlutils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in excel: ", self.rows)

        list_status = []

        for r in range(2, self.rows + 1):
            self.user = xlutils.readData(self.path, 'Sheet1', r, 1)
            self.password = xlutils.readData(self.path, 'Sheet1', r, 2)
            self.exp = xlutils.readData(self.path, 'Sheet1', r, 3)

            self.logger.info(f"Test Row: {r} | Username: {self.user} | Expected: {self.exp}")

            self.driver.get(self.base_url)  # Reload for each test iteration

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "username"))
                )
                self.lp.setUserName(self.user)
                self.lp.setPassword(self.password)
                self.lp.clickLogin()
            except Exception as e:
                self.logger.error(f"Login page not ready or error during login: {e}")
                list_status.append("Fail")
                continue

            # Check if login succeeded by looking for the dashboard element
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//p[@class='oxd-userdropdown-name']"))
                )
                login_success = True
            except:
                login_success = False

            if login_success and self.exp == "pass":
                self.logger.info("*** Passed ***")
                list_status.append("Pass")
                self.hp.logout()
            elif login_success and self.exp == "fail":
                self.logger.info("*** Failed (unexpected login success) ***")
                self.hp.logout()
                list_status.append("Fail")
            elif not login_success and self.exp == "fail":
                self.logger.info("*** Passed (login failed as expected) ***")
                list_status.append("Pass")
            elif not login_success and self.exp == "pass":
                self.logger.info("*** Failed (login should have succeeded) ***")
                list_status.append("Fail")

        if "Fail" not in list_status:
            self.logger.info("Login DDT passed ....")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT failed ....")
            self.driver.close()
            assert False

        self.logger.info("********** END of login DDT Test ************")
        self.logger.info("************* Completed Test_002_DDT_login **************")
