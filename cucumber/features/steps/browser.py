from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import sleep

class Browser():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def openPVS(self):
        self.driver.get("http://localhost:3001")

    
    def login(self):
        usernameText = self.driver.find_element_by_id("username")
        usernameText.clear()
        usernameText.send_keys("test")

        passwordText = self.driver.find_element_by_id("password")
        passwordText.clear()
        passwordText.send_keys("test")

        loginButton = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/header/button')
        loginButton.click()

    def clickProjectCard(self, projectName):
        wait = WebDriverWait(self.driver, 10)
        projectCard = wait.until(EC.presence_of_element_located((By.XPATH, f"//button[.//*[text()='{projectName}']]"))) 
        sleep(5)
        projectCard.click()

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
        return wait.until(EC.presence_of_element_located((By.XPATH, f"(//button[.//*[text()='{projectName}']])[last()]")))

    def getEnteredProjectName(self, projectName):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By.XPATH, f"//h2[text()='{projectName}']")))

    def getSidebarItem(self, buttonName):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By.XPATH, f"//*[@role='button' and .//*[text()='{buttonName}']]")))

    def isSidebarItemExist(self, buttonName):
        try:
            self.driver.find_element_by_xpath(f"//*[@role='button' and .//*[text()='{buttonName}']]")
            return True
        except NoSuchElementException:
            return False

    def isLoadingAnimationShowing(self):
        wait = WebDriverWait(self.driver, 10)
        loadingAnimation = self.driver.find_element_by_xpath(f"//div[contains(@class, 'MuiBackdrop-root')]")
        try:
            wait.until(EC.visibility_of(loadingAnimation))
            return True
        except TimeoutException:
            return False

    def isLoadingAnimationDisappear(self):
        wait = WebDriverWait(self.driver, 10)
        loadingAnimation = self.driver.find_element_by_xpath(f"//div[contains(@class, 'MuiBackdrop-root')]")
        try:
            wait.until(EC.invisibility_of_element(loadingAnimation))
            return True
        except TimeoutException:
            return False

    def isChartExist(self, githubType, title):
        try:
            titleElement = self.driver.find_element_by_xpath(f"//h1[text()='{title}']")
            titleAndChart = self.driver.find_element_by_xpath(f"//*[@id='{title.lower()}-{githubType}-chart']")
            return True
        except NoSuchElementException:
            return False

    def isDropdownWithValueExist(self, value):
        try:
            self.driver.find_element_by_xpath(f"//div[./div[contains(@class, 'MuiSelect-selectMenu')] and ./input[@value='{value}']]")
            return True
        except NoSuchElementException:
            return False

    def wait(self, time):
        sleep(time)








    