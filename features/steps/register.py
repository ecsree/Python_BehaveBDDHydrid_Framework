from behave import *
from features.pageObjects.HomePage import HomePage
from utilities import dynamic_email_generator


# email = dynamic_email_generator.generate_email_with_time_stamp()
# print(email)

@given(u'I navigate to Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()


@when(u'I enter below mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_firstname(row["first_name"])
        context.register_page.enter_lastname(row["last_name"])
        context.register_page.enter_email(dynamic_email_generator.generate_email_with_time_stamp())
        print(dynamic_email_generator.generate_email_with_time_stamp())
        context.register_page.enter_phone_number(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["confirm_password"])
        context.register_page.click_privacy_policy()


@when(u'I click on continue button')
def step_impl(context):
    context.my_account_page = context.register_page.click_continue_button()
    print("i clicked continue button")


@then(u'Account should get created')
def step_impl(context):
    assert context.my_account_page.get_account_created_message("Your Account Has Been Created!") is True


@when(u'I enter all fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_firstname(row["first_name"])
        context.register_page.enter_lastname(row["last_name"])
        context.register_page.enter_email(dynamic_email_generator.generate_email_with_time_stamp())
        context.register_page.enter_phone_number(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["confirm_password"])
        context.register_page.click_newsletter_button()
        context.register_page.click_privacy_policy()


@when(u'I enter all fields with existing email')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_firstname(row["first_name"])
        context.register_page.enter_lastname(row["last_name"])
        context.register_page.enter_email(row["email"])
        context.register_page.enter_phone_number(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_confirm_password(row["confirm_password"])
        context.register_page.click_newsletter_button()
        context.register_page.click_privacy_policy()


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    assert context.register_page.get_duplicate_email_warning("Warning: E-Mail Address is already registered!")


@when(u'I dont enter any details')
def step_impl(context):
    context.register_page.enter_firstname("")
    context.register_page.enter_lastname("")
    context.register_page.enter_email("")
    context.register_page.enter_phone_number("")
    context.register_page.enter_password("")
    context.register_page.enter_confirm_password("")
    # context.register_page.click_privacy_policy()


@then(u'Proper warning messages for every mandatory fields should be display')
def step_impl(context):
    assert context.register_page.get_expected_privacy_warning("Warning: You must agree to the Privacy Policy!") is True
    assert context.register_page.get_expected_firstname_warning(
        "First Name must be between 1 and 32 characters!") is True
    assert context.register_page.get_expected_lastname_warning("Last Name must be between 1 and 32 characters!") is True
    assert context.register_page.get_expected_email_warning("E-Mail Address does not appear to be valid!") is True
    assert context.register_page.get_expected_phone_number_warning(
        "Telephone must be between 3 and 32 characters!") is True
    assert context.register_page.get_expected_password_warning("Password must be between 4 and 20 characters!") is True

    print("all assertions are successfully completed")
