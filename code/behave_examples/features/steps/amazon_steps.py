from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given(u'we are browsing amazon.com')
def step_impl(context):
    browser = webdriver.Chrome()
    context.browser = browser 
    browser.get("https://www.amazon.com")
    time.sleep(4)
    assert "Amazon.com" in browser.title

@when(u'we search for "{target}"')
def step_impl(context, target):
    browser = context.browser
    searchbox = browser.find_element_by_name("field-keywords")
    searchbox.clear()
    searchbox.send_keys(target)
    searchbox.send_keys(Keys.RETURN)
    time.sleep(4)
    assert "Amazon.com" in browser.title    

@then(u'we should see a "{result}"')
def step_impl(context, result):
    browser = context.browser
    assert result in browser.page_source
