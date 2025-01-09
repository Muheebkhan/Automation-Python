import driver

while True:
    # Extract data from the current page
    rows = driver.find_elements("xpath", "//table/tbody/tr")
    for row in rows:
        print(row.text)

    # Check if the "Next" button is enabled
    try:
        next_button = driver.find_element("xpath", "//button[text()='Next']")
        if next_button.is_enabled():
            next_button.click()
        else:
            break
    except:
        break
