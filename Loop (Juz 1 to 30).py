import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# from quranmajeed import reciter_button

driver=webdriver.Chrome()
driver.get("https://quranmajeed.com/")
driver.maximize_window()
time.sleep(2)
print(f'opening form',driver.title)

readquran=driver.find_element(By.CSS_SELECTOR,value=".elementor-button.elementor-button-link.elementor-size-md")
readquran.click()
time.sleep(2)

# juz_btn=driver.find_element(By.CSS_SELECTOR,value="#b_juz").click()
# time.sleep(10)
juzs=driver.find_elements(By.CLASS_NAME,value="perJuzz")
print('total number of juz are:',len(juzs))

for juz in range(len(juzs)):
    juz_btn = driver.find_element(By.CSS_SELECTOR, value="#b_juz")
    juz_btn.click()
    time.sleep(2)
    all_juz=driver.find_element(By.ID,value=f'juz-{juz+1}')
    all_juz.click()
    time.sleep(10)