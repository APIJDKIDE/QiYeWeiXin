from appium import webdriver

from page.base_page import BasePage
from page.main import Main


class App(BasePage):

    def start(self):
        if self._driver == None:
            desired_caps = {}
            desired_caps['appPackage'] = "com.tencent.wework"
            desired_caps["appActivity"] = ".launch.LaunchSplashActivity"  # .launch.WwMainActivity
            desired_caps["platformName"] = "Android"
            desired_caps["deviceName"] = "EJL4C17106004977"
            desired_caps["noReset"] = True
            desired_caps["dontStopAppOnReset"] = True
            desired_caps["skipDeviceInitialization"] = True
            desired_caps["skipUnlock"] = True
            desired_caps["unicodeKeyboard"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)

        return self

    def restart(self):
        return self

    def stop(self):
        return self


    def main(self) ->Main:
        return Main(self._driver)