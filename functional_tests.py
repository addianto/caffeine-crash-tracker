from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Chrome()
browser.get("http://localhost:8000")

element: WebElement = browser.find_element(by=By.TAG_NAME, value="h1")

assert element.text == "Mental Health Tracker"

print("OK")
