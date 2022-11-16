from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver): # how it should be constructed
        self.driver = driver

    #self.driver.find_element(By.ID, "username0").send_keys("gialodadu")
    #self.driver.find_element(By.ID, "password1").send_keys("22Aprili")
    #self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()

    username = (By.XPATH,"//input[@type='text']")
    password = (By.ID, "password1")
    remeber_user_id = (By.XPATH, "//label[@for='rememberuserid']")
    login_button = (By.ID, "accept")
    def get_username(self):
        return self.driver.find_element(*LoginPage.username) # * converts to tuple

    def get_password(self):
        return self.driver.find_element(*LoginPage.password) # * converts to tuple

    def get_remeber_user(self):
        return  self.driver.find_element(*LoginPage.remeber_user_id)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)