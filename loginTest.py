import unittest

from selenium import webdriver

class LoginTest(unittest.TestCase):
    def setUp(self):
        



driver.get("http://localhost:3001")

usernameText = driver.find_element_by_id("user_name")
usernameText.clear
usernameText.send_keys("username")

passwordText = driver.find_element_by_id("password")
passwordText.clear
passwordText.send_keys("password")

loginButton = driver.find_element_by_xpath('//*[@id="root"]/div/div/header/button')
loginButton.click()