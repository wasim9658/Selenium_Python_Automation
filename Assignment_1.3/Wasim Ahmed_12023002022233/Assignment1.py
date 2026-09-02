from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome browser
driver = webdriver.Chrome()

# Open Form Authentication page
driver.get("https://the-internet.herokuapp.com/login")

# Wait for page to load
time.sleep(2)


# Locate username using ID
username = driver.find_element(By.ID, "username")

print("Element located by ID:",
      username.get_attribute("id"))


# Locate password using NAME
password = driver.find_element(By.NAME, "password")

print("Element located by NAME:",
      password.get_attribute("name"))


# Locate heading using TAG_NAME
heading = driver.find_element(By.TAG_NAME, "h2")

print("Element located by TAG_NAME:",
      heading.text)


# Locate link using LINK_TEXT
link = driver.find_element(By.LINK_TEXT, "Elemental Selenium")

print("Element located by LINK_TEXT:",
      link.text)


# Locate element using CLASS_NAME
button = driver.find_element(By.CLASS_NAME, "radius")

print("Element located by CLASS_NAME:",
      button.get_attribute("class"))


# Wait before closing
time.sleep(2)

# Close browser
driver.quit()