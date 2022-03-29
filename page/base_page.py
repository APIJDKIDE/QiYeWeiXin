from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage():

    _black_list = [
        (By.XPATH,"//*[@text = '确认']"),
        (By.XPATH, "//*[@text = '确定']"),
        (By.XPATH, "//*[@text = '下次再说']")
    ]
    def __init__(self,driver:WebDriver = None ):
        self._driver = driver


    def find(self,locator,value:str = None):
        element:WebElement
        try:
            if isinstance(locator,tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator)
            return element
        except:
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist)>0 :
                    elelist[0].click()
                    return self.find(locator,value)





