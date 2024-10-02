from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a Service instance
service = Service(executable_path="msedgedriver.exe")

# Pass the service instance to the Edge webdriver
driver = webdriver.Edge(service=service)

# Open the website
driver.get("https://orteil.dashnet.org/cookieclicker/")

lang_id = "langSelect-EN"
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix= "productPrice"
product_prefix="product"

# Wait for the language selection element
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
lang = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
lang.click()

# Wait for the cookie element
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)

# Loop to click the cookie 100 times, re-fetching the element in each iteration

cookie = driver.find_element(By.ID, cookie_id)  # Re-fetch the cookie element
cookie.click()
 


while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID,cookies_id).text.split(" ")[0]
    cookies_count=int(cookies_count.replace(",", ""))
    print(cookies_count)
    for i in range(4):
        product_price =driver.find_element(By.ID, product_price_prefix +str(i)).text.replace(",","")

        if not product_price.isdigit():
            continue
        product_price=int(product_price)

        if cookies_count>=product_price:
            product = driver.find_element(By.ID,product_prefix + str(i))
            product.click()
            break

# Close the browser
#driver.quit()
