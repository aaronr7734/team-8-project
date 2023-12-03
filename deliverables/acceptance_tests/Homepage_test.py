from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time

# Replace 'path/to/msedgedriver' with the absolute path to your downloaded Microsoft Edge Driver executable
edge_driver_path = 'Documents/CS386/myenv/Scripts/activate/edgedriver_win64/msedgedriver.exe'

# Create EdgeOptions object and set the executable path
edge_options = webdriver.EdgeOptions()
edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Initialize the Edge WebDriver with options
driver = webdriver.Edge(options=edge_options)

# Navigate to the webpage
driver.get("https://www.studentdiscountz.org")

# Function to click on each deal section
def click_deal_section(deal_id):
    deal_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, deal_id)))

    # Use JavaScript to click the element
    driver.execute_script("arguments[0].click();", deal_tab)

    print(f"Clicked on {deal_id} tab")
    time.sleep(1)

# Click on each deal section
deal_sections = ["gadget-deals-tab", "dorm-deals-tab", "book-deals-tab", "food-deals-tab", "fun-deals-tab"]
for section in deal_sections:
    click_deal_section(section)

# Click on each dropdown option under "Majors of Study"
majors_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "navbar-dropdown")))
majors_dropdown.click()

# Wait for the dropdown options to appear
dropdown_options = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "dropdown-item")))

# Define a dictionary mapping option text to page URLs
dropdown_options_mapping = {
    "Art History": "https://www.studentdiscountz.org/ArtHistory.html",
    "Business": "https://www.studentdiscountz.org/Business.html",
    "Computer Science": "https://www.studentdiscountz.org/computerScience.html",
    "Pre-Med": "https://www.studentdiscountz.org/PreMed.html",
    "Psychology": "https://www.studentdiscountz.org/Psychology.html"
}

# Click on each dropdown option
for option_text, page_url in dropdown_options_mapping.items():
    try:
        option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, option_text)))
        option.click()
        print(f"Clicked on dropdown option: {option_text}")
        time.sleep(1)
        # Navigate back to the main page
        driver.get("https://www.studentdiscountz.org") 

        # Click on the next one
        majors_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "navbar-dropdown")))
        majors_dropdown.click()
        time.sleep(1)

    except StaleElementReferenceException:
        print(f"StaleElementReferenceException occurred. Retrying...")
        option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, option_text)))
        option.click()
        print(f"Clicked on dropdown option after retry: {option_text}")

    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

    # Click on the "Login" link
try:
    login_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
    login_link.click()
    print("Clicked on the Login link")
    time.sleep(1)


except TimeoutException as e:
    print(f"TimeoutException occurred: {e}")

# Click on the "Sign Up" link
try:
    signup_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up")))
    signup_link.click()
    print("Clicked on the Sign Up link")
    time.sleep(2)

except TimeoutException as e:
    print(f"TimeoutException occurred: {e}")

# Close the browser
driver.quit()
