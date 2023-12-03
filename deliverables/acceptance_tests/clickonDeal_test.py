from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# The path to your downloaded Microsoft Edge Driver executable
edge_driver_path = 'Documents/CS386/myenv/Scripts/activate/edgedriver_win64/msedgedriver.exe'

# Create EdgeOptions object and set the executable path
edge_options = webdriver.EdgeOptions()
edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Initialize the Edge WebDriver with options
driver = webdriver.Edge(options=edge_options)

# Navigate to the home page
base_url = 'https://www.studentdiscountz.org'
driver.get(base_url)

# List of majors and their respective URLs
majors = {
    'Art History': 'https://www.studentdiscountz.org/ArtHistory.html',
    'Business': 'https://www.studentdiscountz.org/Business.html',
    'Computer Science': 'https://www.studentdiscountz.org/computerScience.html',
    'Pre-Med': 'https://www.studentdiscountz.org/PreMed.html',
    'Psychology': 'https://www.studentdiscountz.org/Psychology.html'
}

# Iterate through each major
for major, major_url in majors.items():
    # Navigate to the major's page
    driver.get(major_url)
    time.sleep(2)
    # Find and click on the "View Deal" button
    try:
        view_deal_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@class="btn btn-primary" and contains(text(), "View Deal")]'))
        )
        view_deal_button.click()
        print(f"\nClicked on the View Deal button on the {major} page\n")
        time.sleep(2)

    except Exception as e:
        print(f"Unable to click on the View Deal button for {major}: {e}")

# Close the browser
driver.quit()
