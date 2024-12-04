from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def init_driver():
    """Initialize the WebDriver and open the login page."""
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(10)
    return driver


def capture_error_message(driver, username, password):
    """Fill in the form, submit, and capture error message."""
    try:
        # Locate input fields and login button
        user_name = driver.find_element(By.NAME, "username")
        user_passport = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        # Clear and input values
        user_name.clear()
        user_passport.clear()
        if username:
            user_name.send_keys(username)
        if password:
            user_passport.send_keys(password)
        
        # Submit the form
        login_button.click()
        
        # Capture error message
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Required'] | //div[contains(@class, 'oxd-alert oxd-alert--error')]"))
        )
        print("Captured error message:", error_message.text)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        time.sleep(3)


# Main script
if __name__ == "__main__":
    driver = init_driver()
    
    print("Test case: Empty username and password")
    capture_error_message(driver, username="", password="")
    
    print("Test case: Incorrect username and password")
    capture_error_message(driver, username="123abc", password="456def")
    
    driver.quit()
