from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open Dynamic Content page
driver.get("https://the-internet.herokuapp.com/dynamic_content")


# 1. ^= means starts with
elem_starts = driver.find_elements(
    By.CSS_SELECTOR,
    "[id^='content']"
)

print("Elements with ID starting with 'content':",
      len(elem_starts))


# 2. $= means ends with
elem_ends = driver.find_elements(
    By.CSS_SELECTOR,
    "[id$='-content']"
)

print("Elements with ID ending with '-content':",
      len(elem_ends))


# 3. *= means contains
elem_contains = driver.find_elements(
    By.CSS_SELECTOR,
    "div[class*='row']"
)

print("Elements with class containing 'row':",
      len(elem_contains))


print("\nCSS Wildcard Examples:")
print("[id^='user_']  -> ID starts with user_")
print("[id$='_name']  -> ID ends with _name")
print("[id*='user']   -> ID contains user")


driver.quit()