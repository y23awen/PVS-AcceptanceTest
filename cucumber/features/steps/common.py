from behave import given, when, then
from browser import Browser

@given(u'I open the browser')
def step_impl(context):
    context.browser = Browser()

@given(u'I go to PVS')
def step_impl(context):
    context.browser.openPVS()

@given(u'I log in')
def step_impl(context):
    context.browser.login()