from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
if "Epic sadface" in error_message.text:
    print("Test Passed")
    print(error_message.text)
else:
    print("Test Failed")

driver.quit()
