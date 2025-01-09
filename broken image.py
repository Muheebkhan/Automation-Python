from selenium import webdriver
import requests

# Initialize WebDriver
driver = webdriver.Chrome()  # Replace with your preferred WebDriver (e.g., Firefox, Edge)
driver.get("https://google.com")  # Replace with the URL of your target webpage

# Find all image elements on the page
images = driver.find_elements("tag name", "img")

# Iterate through each image
for img in images:
    src = img.get_attribute("src")  # Get the image URL
    try:
        # Send a GET request to the image URL
        response = requests.get(src, timeout=5)
        if response.status_code != 200:
            print(f"Broken Image Found: {src} (Status Code: {response.status_code})")
        else:
            print(f"Valid Image: {src}")
    except requests.exceptions.RequestException as e:
        print(f"Error Loading Image: {src}, Error: {e}")

# Quit WebDriver
driver.quit()
