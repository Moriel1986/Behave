from selenium import webdriver
import unittest
import sys
import time
import HtmlTestRunner
from Behave_Framework.pages.fb_login_page import FbLogin
from Behave_Framework.Locators.locators import Locators
sys.path.append("/Users/user/PycharmProjects/Behave/Behave_Framework/Reports")


class FbTest(unittest.TestCase):
    baseURL = "http://wwww.facebook.com"
    username = "Demoriel24@comcast.net"
    password = "Kobelastgame60$"
    driver = webdriver.Chrome(executable_path="/Users/user/Downloads/chromedriver")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = FbLogin(self.driver)
        lp.set_username(self.username)
        lp.set_password(self.password)
        lp.click_login_button()
        time.sleep(3)
        self.assertEqual("Facebook", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print(cls.driver.title, "Test Completed")


if __name__ == '__main__':unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
   (output='/Users/user/PycharmProjects/Behave/Behave_Framework/Reports'))