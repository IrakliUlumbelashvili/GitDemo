from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_end_to_end(self):
        login = LoginPage(self.driver)
        login.get_username().send_keys("DarinaEradze")
        sleep(1)
        login.get_password().send_keys("Ivlisi27!")
        sleep(2)
        login.get_remeber_user().click()
        login.get_login_button().click()
        trade = TradePage(self.driver)
        trade.get_trade_button().click()
        trade.get_symbol().send_keys("TW")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='navigation-symbol-search']").send_keys("AAPL")
        self.driver.find_element(By.ID, "navigation-symbol-search").send_keys(Keys.RETURN)
        #//button[@data-testid='TradeButton-buy']
        #.send_keys(Keys.COMMAND + "a")
        #.send_keys(Keys.DELETE)

        # This is Buy market order
        self.driver.find_element(By.CSS_SELECTOR, "button[direction='sell']").click()
        length = str(self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").get_attribute("value"))
        print(length)
        for quantity in range(len(length)):
            self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys(Keys.BACKSPACE)
        # driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys(Keys.COMMAND + "a")
        # driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys(Keys.DELETE)

        self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys(2)
        self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Order Type']").click()
        # select = Select(driver.find_element(By.CSS_SELECTOR, "button[aria-label='Order Type']"))
        # select.select_by_visible_text('MARKET')
        self.driver.find_element(By.CSS_SELECTOR, "li[data-testid='order-type-dropdown:MARKET']").click()
        sleep(2)
        self.driver.find_element(By.ID, "review-order-button").click()

        self.driver.find_element(By.ID, "send-order-button").click()

        self.driver.find_element(By.XPATH, "//div[text()= 'Notifications']").click()

        original_notification = []
        original_message = [self.driver.find_element(By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]").text]
        print(original_message)
        print(original_notification)
        for records in (original_message):

            original_notification.append(records.strip(" "))

        print(original_notification)
        check_message = "AAPL MKT has been submitted"
        print(check_message)
        assert check_message in original_message
        assert original_message == original_notification
        print("SomeCode")
        print("SomeStuff")
        print("CuTThis")
        print("GitStuffDemo")
        print("MyCHange")

    #Thinkcronization methods are also known as waits . 2 types of waits  1. inplisit 2 explisit waits
    # this waits are designed to wait until element is located present on the page
    #drive.implicitly_wait (19)  - ramdeni xani meicados