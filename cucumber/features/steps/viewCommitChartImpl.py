from selenium import webdriver
import time

class ViewCommitChartImpl():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ViewCommitChartImpl()
        return cls.instance

    # def setUp(self):
    def __init__(self):
        # self.driver = webapp.get_driver()
        self.driver = webdriver.Chrome()

    def openPVS(self):
        self.driver.get("http://localhost:3001")

    
    def addProject(self, projectName, url):
        # usernameText = self.driver.find_element_by_id("user_name")
        usernameText = self.driver.find_element_by_xpath('//*[@id="user_name"]')
        usernameText.clear
        usernameText.send_keys("username")
        # time.sleep(2)

        # passwordText = self.driver.find_element_by_id("password")
        passwordText = self.driver.find_element_by_xpath('//*[@id="password"]')
        passwordText.clear
        passwordText.send_keys("password")

        loginButton = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/header/button')
        loginButton.click()
        time.sleep(2)
        self.driver.close()
        # self.driver.close()

        # self.driver.quit()


# viewCommitChartImpl = ViewCommitChartImpl.get_instance()




    