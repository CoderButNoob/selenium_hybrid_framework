# # import pytest
# # import random
# # import os
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.common.by import By
# # from page_objects.login_page import LoginPage
# # from utilities.read_properties import ReadConfig
# # from utilities.customLogger import LogGen
# # from page_objects.add_employee import addEmployee
# # from page_objects.search_employee import searchEmployee
# #
# # class Test_004_SearchEmployeeByName:
# #     base_url = ReadConfig.getApplicationUrl()
# #     username = ReadConfig.getUsername()
# #     password = ReadConfig.getPassword()
# #
# #     logger = LogGen.loggen()
# #
# #     def test_seacrhEmployeeByName(self,setup):
# #         self.logger.info("**************** Test_004_SearchEmployeeByName **************")
# #         self.driver = setup
# #         self.driver.get(self.base_url)
# #         self.driver.maximize_window()
# #
# #         self.lp = LoginPage(self.driver)
# #         self.lp.setUserName(self.username)
# #         self.lp.setPassword(self.password)
# #         self.lp.clickLogin()
# #         self.logger.info("********** Login Successful ***********")
# #
# #         self.logger.info("*********** Start Searching Employee By Name ***************")
# #
# #         self.add_emp = addEmployee(self.driver)
# #         self.add_emp.clickPIM()
# #         self.add_emp.clickaddEmployeeButton()
# #
# #         self.logger.info("*********** Searching Employee By Name ***************")
# #         searchEmp = searchEmployee(self.driver)
# #         searchEmp.set
#
#
# import pytest
# import random
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from page_objects.login_page import LoginPage
# from utilities.read_properties import ReadConfig
# from utilities.customLogger import LogGen
# from page_objects.add_employee import addEmployee
# from page_objects.search_employee import searchEmployee
# from selenium.common.exceptions import StaleElementReferenceException
#
# class Test_004_SearchEmployeeByName:
#     base_url = ReadConfig.getApplicationUrl()
#     username = ReadConfig.getUsername()
#     password = ReadConfig.getPassword()
#
#     logger = LogGen.loggen()
#
#     def test_seacrhEmployeeByName(self, setup):
#         self.logger.info("**************** Test_004_SearchEmployeeByName **************")
#         self.driver = setup
#         self.driver.get(self.base_url)
#         self.driver.maximize_window()
#
#         self.lp = LoginPage(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         self.logger.info("********** Login Successful ***********")
#
#         self.logger.info("*********** Adding New Employee ***************")
#
#         self.add_emp = addEmployee(self.driver)
#         self.add_emp.clickPIM()
#         self.add_emp.clickaddEmployeeButton()
#
#         first_name = "Aniket"
#         last_name = "Sonar"
#         emp_id = str(random.randint(1000, 9999))
#
#         self.add_emp.addFirstName(first_name)
#         self.add_emp.addMiddleName("")
#         self.add_emp.addLastName(last_name)
#         self.add_emp.addEmpID(emp_id)
#         self.add_emp.click_saveButton()
#
#         self.logger.info(f"*********** Employee Added: {first_name} {last_name}, ID: {emp_id} ***************")
#
#         # Now navigate back to employee list
#         self.logger.info("*********** Navigating to Employee List for Search ***************")
#
#         search_emp = searchEmployee(self.driver)
#         search_emp.click_eployeeList()
#
#         # Search by First Name
#         self.logger.info(f"*********** Searching for Employee by Name: {first_name} ***************")
#         search_emp.searchByName(first_name)
#         search_emp.click_searchButton()
#
#         WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[@class='oxd-table-body']/div[1]"))
#         )
#
#         # wait = WebDriverWait(self.driver, 10)
#
#         # Validate Search Results
#         # page_source = self.driver.page_source
#         # if first_name in page_source and last_name in page_source:
#         #     self.logger.info("*********** Employee Search Test Passed ***************")
#         #     assert True
#         # else:
#         #     self.logger.error("*********** Employee Search Test Failed ***************")
#         #     assert False
#         #
#         # self.driver.close()
#         # self.logger.info("******** Ending Test_004_SearchEmployeeByName *********")
#         rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div")
#         found = False
#         for row in rows:
#             row_text = row.text
#             print("ROW TEXT:", row_text)  # Debug
#             if first_name in row_text:
#                 found = True
#                 break
#
#         if found:
#             self.logger.info("*********** Employee Search Test Passed ***************")
#             assert True
#         else:
#             self.logger.error("*********** Employee Search Test Failed ***************")
#             assert False
#
#         self.logger.info("******** Ending Test_004_SearchEmployeeByName *********")
#         self.driver.close()
#
import time
import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen
from page_objects.add_employee import addEmployee
from page_objects.search_employee import searchEmployee


class Test_004_SearchEmployeeByName:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_seacrhEmployeeByName(self, setup):
        self.logger.info("**************** Test_004_SearchEmployeeByName **************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        # Login
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful ***********")

        # Add new employee
        self.logger.info("*********** Adding New Employee ***************")
        self.add_emp = addEmployee(self.driver)
        self.add_emp.clickPIM()
        self.add_emp.clickaddEmployeeButton()

        first_name = "Shriya"
        last_name = "Sonar"
        emp_id = str(random.randint(1000, 9999))

        self.add_emp.addFirstName(first_name)
        self.add_emp.addMiddleName("")
        self.add_emp.addLastName(last_name)
        self.add_emp.addEmpID(emp_id)
        self.add_emp.click_saveButton()
        time.sleep(10)

        self.logger.info(f"*********** Employee Added: {first_name} {last_name}, ID: {emp_id} ***************")

        # Navigate to Employee List for searching
        self.logger.info("*********** Navigating to Employee List for Search ***************")
        search_emp = searchEmployee(self.driver)
        search_emp.click_eployeeList()

        # Search by First Name
        self.logger.info(f"*********** Searching for Employee by Name: {first_name} ***************")
        search_emp.searchByName(first_name)
        search_emp.click_searchButton()
        time.sleep(10)

        # Wait until search results table is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='oxd-table-body']/div[1]"))
        )

        # Retry logic to handle stale elements
        found = False
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            try:
                rows = self.driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']/div")
                for row in rows:
                    row_text = row.text
                    print("ROW TEXT:", row_text)  # Debug output
                    if first_name.lower() in row_text.lower():
                        found = True
                        break
                break  # success, exit retry loop
            except StaleElementReferenceException:
                attempts += 1
                print(f"StaleElementReferenceException caught. Retrying {attempts}/{max_attempts}")

        # Assert based on found flag
        if found:
            self.logger.info("*********** Employee Search Test Passed ***************")
            assert True
        else:
            self.logger.error("*********** Employee Search Test Failed ***************")
            assert False

        self.logger.info("******** Ending Test_004_SearchEmployeeByName *********")
        self.driver.close()
