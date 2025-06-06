import pytest
import random
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen
from page_objects.add_employee import addEmployee

class Test_003_AddEmployee:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_addEmployee(self,setup):
        self.logger.info("**************** Test_003_AddEmployee **************")
        self.driver=setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********** Login Successful ***********")

        self.logger.info("********** Starting Add Emp Test ***********")

        self.add_emp = addEmployee(self.driver)
        self.add_emp.clickPIM()
        self.add_emp.clickaddEmployeeButton()

        self.logger.info("********** Providing Emp Details ************")
        random_emp_id = str(random.randint(1000000000, 9999999999))
        self.add_emp.addFirstName("Aniket")
        self.add_emp.addMiddleName(" ")
        self.add_emp.addLastName("Soanr")
        self.add_emp.addEmpID(random_emp_id)
        self.add_emp.click_saveButton()

        self.logger.info("************ Saving Emp Details ************")

        self.logger.info("************ Add Emp Validation Started ***********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)

        if "Employee Full Name" in self.msg:
            assert True == True
            self.logger.info("******** Add Customer Test Passed **********")
        else:
            assert True == False

        self.driver.close()
        self.logger.info("******** Ending Test_003_AddEmployee *********")




