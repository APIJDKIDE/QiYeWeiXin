"""
添加成员page
"""
from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class MemberInvite(BasePage):

    def addmember_by_manual(self):
        self.find(MobileBy.XPATH, "//*[@class='android.widget.TextView' and @text = '手动输入添加']").click()
        from page.ContactAdd import ContactAdd
        return ContactAdd(self._driver)


    def get_toast(self):

        pass
