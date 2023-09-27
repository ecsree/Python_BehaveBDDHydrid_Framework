from behave import *
from features.pageObjects.HomePage import HomePage


@given(u'I got navigated to Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.verify_homepage_title("Your Store")


@when(u'I enter valid product like {product} into the search box field')
def step_impl(context, product):
    context.home_page.enter_to_search_box(product)


@when(u'I click on Search button')
def step_impl(context):
    context.home_page.click_search_button()


@then(u'Valid product should get displayed in search results')
def step_impl(context):
    assert context.home_page.verify_product_display()


@when(u'I enter invalid product like {product} into the Search box field')
def step_impl(context, product):
    context.home_page.enter_to_search_box(product)


@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    assert context.home_page.verify_no_product_warning("There is no product that matches the search criteria.")


@when(u'I dont enter anything into Search box field')
def step_impl(context):
    context.home_page.enter_to_search_box("")
