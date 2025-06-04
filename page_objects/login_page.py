# # from selenium import  webdriver
# # from selenium.webdriver.common.by import By
# #
# # driver = webdriver.Chrome()
# # class login:
# #     textbox_username_name = "username"
# #     textbox_password_name = "password"
# #     button_login_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
# #     # logout_link_linktext = "Logout"
# #
# #     def __init__(self,driver):
# #         self.driver = driver
# #
# #     def setUserName(self,username):
# #         self.driver.find_element(By.ID,self.textbox_username_id).clear()
# #         self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
# #
# #     def setPassword(self,password):
# #         self.driver.find_element(By.ID,self.textbox_password_id).clear()
# #         self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
# #
# #     def clickLogin(self):
# #         self.driver.find_element(By.XPATH,self.button_login_xpath).click()
# #
# #     # def clickLogout(self):
# #     #     self.driver.find_element(By.LINK_TEXT,self.logout_link_linktext).click()
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# class LoginPage:
#     textbox_username_name = "username"
#     textbox_password_name = "password"
#     button_login_xpath = "//button[@type='submit']"
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def setUserName(self, username):
#         self.driver.find_element(By.NAME, self.textbox_username_name).clear()
#         self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)
#
#     def setPassword(self, password):
#         self.driver.find_element(By.NAME, self.textbox_password_name).clear()
#         self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element(By.XPATH, self.button_login_xpath).click()
#
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # wait up to 10 seconds

    def setUserName(self, username):
        # Wait until username input is present and visible
        username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_username_name)))
        username_input.clear()
        username_input.send_keys(username)

    def setPassword(self, password):
        password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, self.textbox_password_name)))
        password_input.clear()
        password_input.send_keys(password)

    def clickLogin(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        login_button.click()
