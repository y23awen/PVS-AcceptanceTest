from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep

class Browser():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def openPVS(self):
        self.driver.get("http://localhost:3002")

    
    def login(self):
        usernameText = self.driver.find_element_by_id("username")
        usernameText.clear()
        usernameText.send_keys("test")

        passwordText = self.driver.find_element_by_id("password")
        passwordText.clear()
        passwordText.send_keys("test")

        loginButton = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/header/button')
        loginButton.click()
    
    def enterSelectProjectPage(self):
        self.driver.get("http://localhost:3002/select")

    def clickCreateProjectCard(self):
        wait = WebDriverWait(self.driver, 10)        
        addProjectButton =  wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="create-project-card"]')))
        addProjectButton.click()

    def inputProjectName(self, projectName):
        projectNameText = self.driver.find_element_by_xpath('//*[@id="ProjectName"]')
        projectNameText.clear()
        projectNameText.send_keys(projectName)

    def inputGithubRepositoryUrl(self, url):
        projectUrlText = self.driver.find_element_by_xpath('//*[@id="GithubRepositoryURL"]')
        projectUrlText.clear()
        projectUrlText.send_keys(url)

    def inputSonarRepositoryUrl(self, url):
        projectUrlText = self.driver.find_element_by_xpath('//*[@id="SonarRepositoryURL"]')
        projectUrlText.clear()
        projectUrlText.send_keys(url)

    def clickCreateProjectButton(self):
        wait = WebDriverWait(self.driver, 10)        
        createButton = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="CreateProjectBtn"]')))
        createButton.click()
        
    def acceptInputErrorAlert(self, errorMessage):
        WebDriverWait(self.driver, 3).until(EC.alert_is_present(), errorMessage)
        alert = Alert(self.driver)
        if alert.text != errorMessage:
            raise AssertionError("Error Message not matching")
        alert.accept()

    def acceptInputErrorAlertWithoutCheckingMessage(self):
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        alert = Alert(self.driver)
        alert.accept()

    def getProjectCard(self, projectName):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[text()=\'{projectName}\']')))

    def wait(self, time):
        sleep(time)








    