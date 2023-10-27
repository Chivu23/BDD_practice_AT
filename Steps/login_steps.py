from behave import *


@given("I am on the ebay login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when("I insert the correct username and password")
def step_impl(context):
    context.login_page.insert_correct_username()
    context.login_page.insert_correct_password()


@when("I click login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("I can login in the application")
def step_impl(context):
    context.index_page.check_current_url()