import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Quran Majeed website
driver.get("https://quranmajeed.com/")

# Print the page title
print("Title of the page is:", driver.title)

# Maximize the browser window
driver.maximize_window()

# Click on the "Read Quran" button
time.sleep(5)
try:
    read_quran_button = driver.find_element(By.CLASS_NAME, "elementor-button-text")
    read_quran_button.click()
    print("Clicked on 'Read Quran' button")
except Exception as e:
    print(f"Error clicking 'Read Quran' button: {e}")

time.sleep(5)

# Loop through Juz 1 to 30
for juz_number in range(1, 31):
    try:
        # Open the Juz dropdown
        juz_dropdown = driver.find_element(By.ID, "b_juz")
        juz_dropdown.click()
        print("Opened Juz dropdown")

        time.sleep(2)  # Wait for dropdown options to load

        # Select a specific Juz based on its number
        juz_option = driver.find_element(By.XPATH, f"//li[text()='Juz {juz_number}']")
        juz_option.click()
        print(f"Selected Juz {juz_number}")

        time.sleep(2)  # Wait for the content of the Juz to load

    except Exception as e:
        print(f"Error selecting Juz {juz_number}: {e}")

# Close the browser
time.sleep(5)
driver.quit()
