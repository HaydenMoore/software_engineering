from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = None

def setup_module(module):
    global browser
    browser = webdriver.Chrome()
    browser.get("http://www.amazon.com")

def teardown_module(module):
    time.sleep(10)
    if browser:
        browser.close()

def test_did_we_get_to_amazon():
    assert "Amazon" in browser.title

def test_is_cuisinart_a_displayed_coffee_maker():
    id = "twotabsearchtextbox"
    searchbox = browser.find_element_by_id(id)
    searchbox.clear()
    searchbox.send_keys("coffee maker")
    searchbox.send_keys(Keys.RETURN)
    time.sleep(10)
    id="s-results-list-atf"
    result_list = browser.find_element_by_id(id)
    result_text = result_list.text
    assert "Cuisinart" in result_text