import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:3001")

usernameText = driver.find_element_by_id("user_name")
usernameText.clear
usernameText.send_keys("username")

passwordText = driver.find_element_by_id("password")
passwordText.clear
passwordText.send_keys("password")

loginButton = driver.find_element_by_xpath('//*[@id="root"]/div/div/header/button')
loginButton.click()

time.sleep(1)

driver.get_current_url()


driver.close()