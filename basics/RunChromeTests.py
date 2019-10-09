from selenium import webdriver

class RunChromeTests():

    def test(self):
        driver = webdriver.Chrome(executable_path='../venv/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')
        driver.get('http://www.letskodeit.com')

chrome = RunChromeTests()
chrome.test()