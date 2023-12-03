from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'path/to/msedgedriver' with the absolute path to your downloaded Microsoft Edge Driver executable
edge_driver_path = 'Documents/CS386/myenv/Scripts/activate/edgedriver_win64/msedgedriver.exe'

# Create EdgeOptions object and set the executable path
edge_options = webdriver.EdgeOptions()
edge_options.binary_location = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' 

# Initialize the Edge WebDriver with options
driver = webdriver.Edge(options=edge_options)

# Navigate to the website
driver.get('https://www.studentdiscountz.org')

# Find and click on the "Contact Us" link in the footer
contact_us_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="footer"]/a[@href="ContactUsPage.html"]'))
)
contact_us_link.click()

github_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="mission-statement"]//a[@href="https://github.com/aaronr7734/team-8-project"]'))
)

# click on github link
github_link.click()

# Close the browser
driver.quit()
