from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Replace 'path/to/msedgedriver' with the absolute path to your downloaded Microsoft Edge Driver executable
edge_driver_path = 'Documents/CS386/myenv/Scripts/activate/edgedriver_win64/msedgedriver.exe'

# Create EdgeOptions object and set the executable path
edge_options = webdriver.EdgeOptions()
edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Initialize the Edge WebDriver with options
driver = webdriver.Edge(options=edge_options)

# Navigate to the homepage
driver.get('https://www.studentdiscountz.org')

# Click on the Sign Up button
try:
    # Click on the Sign Up button
    signup_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="SignUpPage.html"]'))
    )
    signup_link.click()

    # Fill out the sign-up form
    firstname_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'firstname'))
    )
    lastname_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'lastname'))
    )
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email'))
    )
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    confirmPassword_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'confirmPassword'))
    )

    # Replace with your desired sign-up information
    firstname_input.send_keys("Fakefirstname")
    lastname_input.send_keys("Fakelastname")
    email_input.send_keys("Fake.user@email.edu")
    password_input.send_keys("fakePassword_123")
    confirmPassword_input.send_keys("fakePassword_123")

    # Submit the sign-up form
    print("Waiting for submit button to be clickable")

    signup_submit_button = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="Submit"]'))
    )
    print("Submit button is clickable, clicking now")
    signup_submit_button.click()

    print("Signed up successfully!")


finally:
    # Close the browser
    driver.quit()

