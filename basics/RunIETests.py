from selenium import webdriver

class RunIETests():

    def testMethod(self):
        #initiate the driver instance
        driver = webdriver.Ie(executable_path="../venv/Lib/site-packages/selenium/webdriver/ie/IEDriverServer.exe")

        driver.get('http://www.letskodeit.com')

ff = RunIETests()
ff.testMethod()
