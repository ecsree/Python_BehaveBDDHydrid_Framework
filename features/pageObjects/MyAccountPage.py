from selenium.webdriver.common.by import By

from features.pageObjects.BasePage import BasePage


class MyAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_element = "//a[text()='Edit your account information']"
    account_created_message_xpath = "//div[@id='content']/h1"

    def verify_logged_in(self):
        return self.driver.find_element(By.XPATH, self.my_account_element).is_displayed()

    def get_account_created_message(self, expected_text):
        return self.display_status_of_text("account_created_message_xpath", self.account_created_message_xpath, expected_text)
