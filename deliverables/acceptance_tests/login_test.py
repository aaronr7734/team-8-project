from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Replace 'path/to/msedgedriver' with the absolute path to your downloaded Microsoft Edge Driver executable
edge_driver_path = 'Documents/CS386/myenv/Scripts/activate/edgedriver_win64/msedgedriver.exe'

# Create EdgeOptions object and set the executable path
edge_options = webdriver.EdgeOptions()
edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' 

# Initialize the Edge WebDriver with options
driver = webdriver.Edge(options=edge_options)

# Navigate to the login page
driver.get('https://www.studentdiscountz.org')

# Click on the Login button
try:
    # Navigate to the login page
    driver.get('https://www.studentdiscountz.org')

    # Click on the Login button
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="LoginPage.html"]'))
    )
    login_link.click()

    # Fill out the login form
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )

    # Replace with your existing account information
    email_input.send_keys("fake.email@example.edu")
    password_input.send_keys("fakePassword_123")

    # Submit the login form
    login_submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Submit"]'))
    )
    login_submit_button.click()

    # Introduce a delay after submitting the form (5 seconds in this example)
    time.sleep(5)

    print("Logged in successfully!")

except TimeoutException as e:
    print(f"Timeout waiting for element: {str(e)}")
except Exception as e:
    print(f"Error: {str(e)}")

finally:
    # Close the browser
    driver.quit()
