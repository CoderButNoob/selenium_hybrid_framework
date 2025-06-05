from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    profile_icon_xpath = "//span[@class='oxd-userdropdown-tab']"
    logout_button_xpath = "//a[text()='Logout']"

    def clickProfileIcon(self):
        self.driver.find_element(By.XPATH, self.profile_icon_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()

    def logout(self):
        self.clickProfileIcon()
        self.clickLogout()
