from selenium import webdriver

class RunFFTests():

    def testMethod(self):
        #initiate the driver instance
        driver = webdriver.Firefox(executable_path="../venv/Lib/site-packages/selenium/webdriver/firefox/geckodriver.exe")

        driver.get('http://www.letskodeit.com')

ff = RunFFTests()
ff.testMethod()
