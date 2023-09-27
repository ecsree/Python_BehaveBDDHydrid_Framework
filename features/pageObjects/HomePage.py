from selenium.webdriver.common.by import By

from features.pageObjects.BasePage import BasePage
from features.pageObjects.LoginPage import LoginPage
from features.pageObjects.RegisterPage import RegisterPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"
    search_box_name = "search"
    search_button_xpath = "//span/button[@type = 'button']"
    product_display_link_text = "HP LP3065"
    no_product_warning = "//p[2]"

    def click_on_my_account(self):
        self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        return LoginPage(self.driver)

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_link_text).click()
        return RegisterPage(self.driver)

    def verify_homepage_title(self, expected_title ):
        return self.driver.title.__eq__(expected_title)

    def enter_to_search_box(self, search_word):
        self.type_into_element("search_box_name", self.search_box_name, search_word)

    def click_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)

    def verify_product_display(self):
        return self.driver.find_element(By.LINK_TEXT, self.product_display_link_text).is_displayed()

    def verify_no_product_warning(self, expected_message):
        return self.driver.find_element(By.XPATH, self.no_product_warning).text.__eq__(expected_message)

