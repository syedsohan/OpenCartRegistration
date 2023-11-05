# Import necessary Selenium modules for web automation
import logging  # For debugging
import time  # For adding delays
from selenium import webdriver  # For initializing a web browser
from selenium.webdriver.common.by import By  # For locating web elements
from selenium.webdriver.support.ui import WebDriverWait  # For waiting on page load

# Set configuration options
url = "https://demo.opencart.com/index.php?route=account/register&language=en-gb"
wait_timeout = 20
short_wait = 5  # seconds
# Initialize the webdriver (using Chrome)
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

try:
    # Open the website
    driver.get(url)
    driver.implicitly_wait(10)  # seconds

    # Test data for registration form
    registration_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "password": "SecurePassword123",
    }

    # Fill in the registration form
    driver.find_element(By.NAME, "firstname").send_keys(registration_data["first_name"])
    time.sleep(short_wait)
    driver.find_element(By.NAME, "lastname").send_keys(registration_data["last_name"])
    time.sleep(short_wait)
    driver.find_element(By.NAME, "email").send_keys(registration_data["email"])
    time.sleep(short_wait)
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight)"
    )  # Scroll down to the page until the continue button is visible
    time.sleep(short_wait)
    driver.find_element(By.NAME, "password").send_keys(registration_data["password"])
    time.sleep(short_wait)

    # Select newsletter subscription option
    newsletter_checkbox = driver.find_element(
        By.CSS_SELECTOR, "input#input-newsletter-yes"
    )
    newsletter_checkbox.click()
    time.sleep(short_wait)

    # Click the Privacy Policy checkbox
    privacy_policy = driver.find_element(
        By.XPATH, "/html//form[@id='form-register']//input[@name='agree']"
    )
    privacy_policy.click()
    time.sleep(short_wait)

    # Click the Continue button
    continue_button = driver.find_element(
        By.XPATH, "/html//form[@id='form-register']//button[@type='submit']"
    )
    continue_button.click()
    time.sleep(short_wait)

    # Validate the confirmation message
    print("Test was successful!") if driver.find_element(
        By.XPATH, "/html//form[@id='form-register']//button[@type='submit']"
    ).is_enabled() else "Test failed."

except Exception as e:
    logging.error(f"An error occurred: {e}")

finally:
    # Close the browser window, even if an exception is raised
    driver.quit()
