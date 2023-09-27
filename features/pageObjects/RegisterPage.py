from selenium.webdriver.common.by import By

from features.pageObjects.BasePage import BasePage
from features.pageObjects.MyAccountPage import MyAccountPage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    firstname_textbox_xpath = "//input[@id='input-firstname']"
    lastname_textbox_xpath = "//input[@id='input-lastname']"
    email_textbox_xpath = "//input[@id='input-email']"
    telephone_textbox_xpath = "//input[@id='input-telephone']"
    password_textbox_xpath = "//input[@id='input-password']"
    confirm_password_textbox_xpath = "//input[@id='input-confirm']"
    news_letter_button_xpath = "//div//input[@name='newsletter'][@value='1']"
    privacy_policy_button_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    duplicate_email_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    expected_privacy_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    expected_firstname_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    expected_lastname_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    expected_email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    expected_telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    expected_password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_firstname(self, firstname):
        self.type_into_element("firstname_textbox_xpath", self.firstname_textbox_xpath, firstname)

    def enter_lastname(self, lastname):
        self.type_into_element("lastname_textbox_xpath", self.lastname_textbox_xpath, lastname)

    def enter_email(self, email):
        self.type_into_element("email_textbox_xpath", self.email_textbox_xpath, email)

    def enter_phone_number(self, phone_number):
        self.type_into_element("telephone_textbox_xpath", self.telephone_textbox_xpath, phone_number)

    def enter_password(self, password):
        self.type_into_element("password_textbox_xpath", self.password_textbox_xpath, password)

    def enter_confirm_password(self, password):
        self.type_into_element("confirm_password_textbox_xpath", self.confirm_password_textbox_xpath, password)

    def click_newsletter_button(self):
        self.click_on_element("news_letter_button_xpath", self.news_letter_button_xpath)

    def click_privacy_policy(self):
        self.click_on_element("privacy_policy_button_xpath", self.privacy_policy_button_xpath)

    def click_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        return MyAccountPage(self.driver)

    def get_duplicate_email_warning(self, duplicate_email_warning_message):
        return self.display_status_of_text("duplicate_email_warning_xpath", self.duplicate_email_warning_xpath,
                                           duplicate_email_warning_message)

    def get_expected_privacy_warning(self, expected_warning):
        return self.display_status_of_text("expected_privacy_warning_xpath", self.expected_privacy_warning_xpath,
                                           expected_warning)

    def get_expected_firstname_warning(self, expected_warning):
        return self.display_status_of_text("expected_firstname_warning_xpath", self.expected_firstname_warning_xpath,
                                           expected_warning)

    def get_expected_lastname_warning(self, expected_warning):
        return self.display_status_of_text("expected_lastname_warning_xpath", self.expected_lastname_warning_xpath,
                                           expected_warning)

    def get_expected_email_warning(self, expected_warning):
        return self.display_status_of_text("expected_email_warning_xpath", self.expected_email_warning_xpath,
                                           expected_warning)

    def get_expected_phone_number_warning(self, expected_warning):
        return self.display_status_of_text("expected_telephone_warning_xpath", self.expected_telephone_warning_xpath,
                                           expected_warning)

    def get_expected_password_warning(self, expected_warning):
        return self.display_status_of_text("expected_password_warning_xpath", self.expected_password_warning_xpath,
                                           expected_warning)
