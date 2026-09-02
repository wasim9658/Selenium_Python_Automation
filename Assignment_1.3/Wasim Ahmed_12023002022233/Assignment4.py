from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome browser
driver = webdriver.Chrome()

# Open website
driver.get("https://the-internet.herokuapp.com/")


# 1. Locate child elements using CSS selector
# a is a child of li, and li is a child of ul

child_elements = driver.find_elements(
    By.CSS_SELECTOR,
    "ul > li > a"
)

print("First 5 child elements:")

for el in child_elements[:5]:
    print(el.text)


# 2. Locate the first child link
specific_link = driver.find_element(
    By.CSS_SELECTOR,
    "ul > li:nth-child(1) > a"
)

print("\nFirst child link:", specific_link.text)


# Close browser
driver.quit()