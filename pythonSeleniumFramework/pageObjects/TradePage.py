from selenium.webdriver.common.by import By


class TradePage:
    def __init__(self,driver):
        self.driver = driver
    trade_button = (By.XPATH, "//button[@data-testid='trade-page-button']")
    symbol = (By.ID, "navigation-symbol-search")
    symbol_lookup = (By.XPATH, "//span[text()='TRADEWEB MARKETS INC COM CL A']")


    def get_trade_button(self):
        return self.driver.find_element(*TradePage.trade_button)

    def get_symbol(self):
        return self.driver.find_element(*TradePage.symbol)

    def get_symbol_lookup(self):
        return self.driver.find_element(*TradePage.symbol_lookup)