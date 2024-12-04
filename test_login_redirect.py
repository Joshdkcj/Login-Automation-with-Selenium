from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Set implicit wait
driver.implicitly_wait(10)

# Input username and password
user_name = driver.find_element(By.NAME, "username")
user_name.send_keys("Admin")

user_password = driver.find_element(By.NAME, "password")
user_password.send_keys("admin123")

# Click the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Validate redirection to the correct URL
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
if driver.current_url == expected_url:
    print("Redirection successful: URL is correct.")
else:
    print(f"Redirection failed: Current URL is {driver.current_url}.")

# End test
time.sleep(3)
driver.quit()