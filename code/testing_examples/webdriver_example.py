from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

try:
    browser.get("http://www.python.org")
    assert "Python" in browser.title
    searchbox = browser.find_element_by_name("q")
    searchbox.clear()
    searchbox.send_keys("pydasdasdacon")
    searchbox.send_keys(Keys.RETURN)
    assert "No results found." in browser.page_source
    time.sleep(5)
    browser.get("http://www.python.org")
    assert "Python" in browser.title
    searchbox = browser.find_element_by_name("q")
    searchbox.clear()
    searchbox.send_keys("pycon")
    searchbox.send_keys(Keys.RETURN)
    assert "No results found." not in browser.page_source
finally:
    print("Closing in 10 seconds...")
    time.sleep(30)
    browser.close()