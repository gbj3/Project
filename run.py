import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Specify the URL
url = "https://www.merfolkslullaby.com/map?&tab=weather"

# Set up the Selenium webdriver
options = Options()
options.add_argument("--headless")  # Run in headless mode, without opening a browser window
service = Service('path/to/chromedriver')  # Replace 'path/to/chromedriver' with the actual path to the ChromeDriver executable
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the webpage
driver.get(url)

# Wait for the data to load
time.sleep(10)  # Adjust the delay as needed

# Extract the desired data
content = driver.page_source

# Specify the output file name
output_file = "codeoutput.txt"

# Write the content to the output file with UTF-8 encoding
with open(output_file, "w", encoding="utf-8") as file:
    file.write(content)

print(f"Output saved to '{output_file}'")

# Close the browser
driver.quit()
