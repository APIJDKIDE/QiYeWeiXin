"""
手动添加成员页面
"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

from page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self,name):
        name_element = self.find(MobileBy.XPATH, "//*[@text ='姓名　']/..//*[@text  = '必填']")
        name_element.send_keys(name)
        return self

    def input_gender(self):
        self.find(MobileBy.XPATH, "//*[@text ='性别']/..//*[@text  = '男']").click()
        self.find(MobileBy.XPATH, "//*[@text = '男']/../..").click()
        return self

    def input_phonenumber(self):
        mobilePhone_element = self.find(MobileBy.XPATH, "//*[@text ='手机　']/..//*[@text  = '手机号']")
        mobilePhone_element.send_keys("12312312312")
        return self

    def click_save(self):
        TouchAction(self._driver).press(x=727, y=1338).move_to(x=730, y=716).release().perform()
        self.find(MobileBy.XPATH,"//*[@text = '保存']").click()
        from page.MemberInvite import MemberInvite  #局部导入。针对循环导入的问题
        return MemberInvite()
