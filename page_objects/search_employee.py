import  time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class searchEmployee:
    employee_list_xpath = "//a[normalize-space()='Employee List']"
    emp_name_xpath = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    emp_id_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
    search_button_xpath = "//button[normalize-space()='Search']"


    # table_xpath = "//div[@role='table']"
    # table_rows_xpath = "//div[@role='row']"


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_eployeeList(self):
        click_eList = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.employee_list_xpath)))
        click_eList.click()

    def searchByName(self,f_name):
        serch_byFname = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.emp_name_xpath)))
        serch_byFname.send_keys(f_name)

    def serachByID(self,e_id):
        search_eID = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.emp_id_xpath)))
        search_eID.send_keys(e_id)

    def click_searchButton(self):
        search_button = self.wait.until(EC.visibility_of_element_located((By.XPATH,self.search_button_xpath)))
        search_button.click()







