#Making a google search


from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a Service instance
service = Service(executable_path="msedgedriver.exe")

# Pass the service instance to the Edge webdriver
driver = webdriver.Edge(service=service)

# Open the Google website
driver.get("https://www.google.com/")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME,"gLFyf"))
)
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("tech with tim" +Keys.ENTER)



WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,"Tech with tim"))
)
link =driver.find_element(By.PARTIAL_LINK_TEXT,"Tech with tim")
link.click


# Wait for 10 seconds
time.sleep(10)

# Close the browser
driver.quit()
