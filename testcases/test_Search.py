import pytest
from appium import webdriver
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

logging.basicConfig(level= logging.INFO)

@pytest.mark.skip
class TestSearch():

    def setup(self):
        desired_caps = {}
        desired_caps['appPackage'] = "com.tencent.wework"
        desired_caps["appActivity"] =".launch.LaunchSplashActivity"  #.launch.WwMainActivity
        desired_caps["platformName"] ="Android"
        desired_caps["deviceName"] ="EJL4C17106004977"
        desired_caps["noReset"] = True
        desired_caps["dontStopAppOnReset"] = True
        desired_caps["skipDeviceInitialization"] = True
        desired_caps["skipUnlock"] = True
        desired_caps["unicodeKeyboard"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_addContact(self):
        #进入添加成员页面
        self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.TextView' and @text = '通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.TextView' and @text = '添加成员...']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.TextView' and @text = '手动输入添加']").click()
        name_element = self.driver.find_element(MobileBy.XPATH, "//*[@text ='姓名　']/..//*[@text  = '必填']")
        name_element.send_keys('test02')
        self.driver.find_element(MobileBy.XPATH, "//*[@text ='性别']/..//*[@text  = '男']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text = '男']/../..").click()
        mobilePhone_element = self.driver.find_element(MobileBy.XPATH, "//*[@text ='手机　']/..//*[@text  = '手机号']")
        mobilePhone_element.send_keys("12312312312")

        TouchAction(self.driver).press(x=727, y=1338).move_to(x=730, y=716).release().perform()

        self.driver.find_element(MobileBy.XPATH,"//*[@text = '保存']").click()


if __name__ == "__main__":
    pytest.main()