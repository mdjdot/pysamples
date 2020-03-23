#!/usr/bin/env python3
"""
http://appium.io/docs/cn/about-appium/intro/
https://github.com/appium/appium-desktop
"""

#!/usr/bin/env python3
from appium import webdriver
import time
import unittest


class TestNativeApp(unittest.TestCase):
    def setUp(self):
        des = {
            "platformName": "Android",
            "platformVersion": "5.1",
            "deviceName": "810EBLS24YG7",
            "appPackage": "com.meizu.flyme.calculator",
            "appActivity": ".Calculator",
            "unicodeKeyboard": True,
            "resetKeyboard": True,
            "skipServerInstallation": True,
            "skipDeviceInitialization": True,
        }
        self.driver = webdriver.Remote(
        'http://localhost:4723/wd/hub', desired_capabilities=des)

    def tearDown(self):
        return self.driver.quit()

    def testAdd(self):
        try:
            time.sleep(10)
            el2 = self.driver.find_element_by_id(
                "com.meizu.flyme.calculator:id/digit1")
            el2.click()
            el3 = self.driver.find_element_by_accessibility_id("+")
            el3.click()
            el3.click()
            el4 = self.driver.find_element_by_id(
                "com.meizu.flyme.calculator:id/digit3")
            el4.click()
            el5 = self.driver.find_element_by_accessibility_id(
                "等号")
            el5.click()
            time.sleep(3)
            result = self.driver.find_element_by_id(
                "com.meizu.flyme.calculator:id/edit_text").text
            self.assertEqual("4", result, "")
            time.sleep(15)
        except Exception as e:
            print(e) 
            self.fail(e)

if __name__ == "__main__":
    unittest.main()
