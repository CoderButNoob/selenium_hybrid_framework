import  time
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class addEmployee:
    pim_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_employee_xpath = "//a[normalize-space()='Add Employee']"
    add_firstname_xpath = "//input[@placeholder='First Name']"
    add_middlename_xpath = "//input[@placeholder='Middle Name']"
    add_lastname_xpath = "//input[@placeholder='Last Name']"
    add_empID_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    save_button_xpath = "//button[normalize-space()='Save']"

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def clickPIM(self):
        click_pim = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.pim_xpath)))
        click_pim.click()

    def clickaddEmployeeButton(self):
        addEmpButton = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.add_employee_xpath)))
        addEmpButton.click()

    def addFirstName(self,f_name):
        first_name = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.add_firstname_xpath)))
        first_name.send_keys(f_name)

    def addMiddleName(self,m_name):
        middle_name = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.add_middlename_xpath)))
        middle_name.send_keys(m_name)

    def addLastName(self,l_name):
        last_name = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.add_lastname_xpath)))
        last_name.send_keys(l_name)

    def addEmpID(self,e_id):
        emp_id = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.add_empID_xpath)))
        emp_id.send_keys(e_id)

    def click_saveButton(self):
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.save_button_xpath)))
        save_button.click()
