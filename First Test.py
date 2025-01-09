from selenium import webdriver
from selenium.webdriver.support.expected_conditions import title_is

browser = webdriver.Firefox()
browser.get("http://chrome.com/")
browser.maximize_window()
title = browser.title
print(title)
assert "selenium" in title