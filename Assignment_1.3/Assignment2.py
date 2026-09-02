from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

# Find all links and print their text
all_links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total links found: {len(all_links)}")

for link in all_links:
    text = link.text.strip()
    if text: # avoid empty
        print(text, "->", link.get_attribute("href"))

driver.quit()