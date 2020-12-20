from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

class Browser():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def openPVS(self):
        self.driver.get("http://localhost:3001")

    
    def login(self):
        usernameText = self.driver.find_element_by_id("user_name")
        usernameText.clear()
        usernameText.send_keys("username")

        passwordText = self.driver.find_element_by_id("password")
        passwordText.clear()
        passwordText.send_keys("password")

        loginButton = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/header/button')
        loginButton.click()
    
    def enterSelectProjectPage(self):
        self.driver.get("http://localhost:3001/select")

    def clickCreateProjectCard(self):
        addProjectButton = self.driver.find_element_by_id('create-project-card')
        addProjectButton.click()

    def inputProjectName(self, projectName):
        projectNameText = self.driver.find_element_by_xpath('//*[@id="ProjectName"]')
        projectNameText.clear()
        projectNameText.send_keys(projectName)

    def inputProjectUrl(self, url):
        projectUrlText = self.driver.find_element_by_xpath('//*[@id="RepositoryURL"]')
        projectUrlText.clear()
        projectUrlText.send_keys(url)

    def clickCreateProjectButton(self):
        createButton = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/button[2]')
        createButton.click()

    def getProjectCard(self, projectName):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[text()=\'{projectName}\']')))

    def wait(self, time):
        sleep(time)








    