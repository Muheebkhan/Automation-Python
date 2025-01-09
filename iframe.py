#import time
from sqlite3 import Time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Firefox WebDriver
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://the-internet.herokuapp.com/iframe")

# Switch to the iframe
iframe = browser.find_element(By.ID, "mce_0_ifr")
browser.switch_to.frame(iframe)

# Interact with the text editor
Text_Editor = browser.find_element(By.ID, "tinymce")

Text_Editor.send_keys("This is Selenium with Python Iframe Tutorial")

# Pause to observe the result
Time.sleep(10)

# Optional: Quit the browser after observation
browser.quit()
