import time
from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open a URL
driver.get("https://quranmajeed.com/")

# Print the page title
print("Title of the page is:", driver.title)

driver.maximize_window()

# Close the browser
sleep(5)

readQuran = driver.find_element(By.CLASS_NAME,value="elementor-button-text").click()

time.sleep(5)

juz = driver.find_element(By.ID,value="b_juz").click()
time.sleep(5)

readQuran = driver.find_element(By.__text_signature__,value="elementor-button-text").click()

juz = driver.find_element(By.ID,value="b_juz").click()
time.sleep(5)






