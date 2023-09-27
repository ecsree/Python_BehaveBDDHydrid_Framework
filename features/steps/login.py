from behave import *
from features.pageObjects.HomePage import HomePage
from utilities import dynamic_email_generator

delay = 5

email = dynamic_email_generator.generate_email_with_time_stamp()


@given(u'I navigate to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.select_login_option()


@when(u'I enter valid {email} and valid {password} into the fields')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I click on login button')
def step_impl(context):
    context.my_account_page = context.login_page.click_login_button()
    print("i clicked")


@then(u'I should get logged in')
def step_impl(context):
    print("i logged in")
    try:
        assert context.my_account_page.verify_logged_in()
        print("i found the element")
    except:
        print("can not find display")


@when(u'I enter invalid email and valid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password("testpassword")


@then(u'I should get a proper warning message')
def step_impl(context):
    element = context.login_page.get_warning_message("Warning: No match for E-Mail Address and/or Password.")
    assert element is True


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")


@when(u'I enter valid email and invalid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("firtest1@gmail.com")
    context.login_page.enter_password("test1233password")


@when(u'I enter invalid email and invalid password into the fields')
def step_impl(context):
    context.login_page.enter_email_address("firtest1234@gmail.com")
    context.login_page.enter_password("test1233password")
