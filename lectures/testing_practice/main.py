from selenium import webdriver
import requests

driver = webdriver.Chrome("driver\chromedriver.exe")

driver.get("https://www.wikipedia.org/")


input_field = driver.find_element(by="id", value="searchInput")
input_field.click()
input_field.send_keys("Ukraine")

elem = driver.find_element(by="class name", value="pure-button.pure-button-primary-progressive")
elem.click()
pass