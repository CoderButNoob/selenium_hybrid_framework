import time
import pytest
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen
from page_objects.add_employee import addEmployee
from page_objects.search_employee import searchEmployee


class Test_005_SearchEmployeeByID:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_seacrhEmployeeById(self, setup):
        self.logger.info("**************** Test_005_SearchEmployeeById **************")
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
        self.logger.info(f"*********** Searching for Employee by Name: {emp_id  } ***************")
        search_emp.serachByID(emp_id)
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

        self.logger.info("******** Ending Test_005_SearchEmployeeById *********")
        self.driver.close()
