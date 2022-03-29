"""
通讯录page
"""
from appium.webdriver.common.mobileby import MobileBy

from page.MemberInvite import MemberInvite
from page.base_page import BasePage


class AddressList(BasePage):

    def add_member(self):
        self.find(MobileBy.XPATH, "//*[@class='android.widget.TextView' and @text = '添加成员...']").click()
        return MemberInvite(self._driver )
