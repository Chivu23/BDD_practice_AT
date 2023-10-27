from browser import Browser
from Pages.login_page import LoginPage
from Pages.index_page import IndexPage


def before_all(context):
    """
    definim....
    """
    context.browser = Browser()
    context.login_page = LoginPage()
    context.index_page = IndexPage()


def after_all(context):
    context.browser.close()