from selenium.webdriver.common.by import By
from features.pageObjects.BasePage import BasePage
from features.pageObjects.MyAccountPage import MyAccountPage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_textbox_id = "input-email"
    password_textbox_id = "input-password"
    login_button_xpath = "//div//input[@value='Login']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_address(self, email):
        self.type_into_element("email_textbox_id", self.email_textbox_id, email)

    def enter_password(self, password):
        self.type_into_element("password_textbox_id", self.password_textbox_id, password)

    def click_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return MyAccountPage(self.driver)

    def get_warning_message(self, expected_warning_message):
        return self.display_status_of_text("warning_message_xpath", self.warning_message_xpath, expected_warning_message)
