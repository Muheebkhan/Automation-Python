from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup WebDriver
driver = webdriver.Chrome()  # Replace with the driver for your browser
driver.get("https://google .com")

# Collect all links on the page
links = driver.find_elements(By.TAG_NAME, "a")  # This returns a list of web elements

# Print and click each link
for index, link in enumerate(links):
    href = link.get_attribute("href")
    print(f"Link {index + 1}: {href}")

    # Optional: Click the link (can be used with logic for testing)
    # link.click()
    # time.sleep(2)
    # driver.back()

# Close the browser
driver.quit()
