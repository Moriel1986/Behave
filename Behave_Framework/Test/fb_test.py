from selenium import webdriver
import unittest
import sys
import time
import HtmlTestRunner
from Behave_Framework.Pages.fb_login_page import FbLogin
sys.path.append("/Users/user/PycharmProjects/Behave/Behave_Framework/Reports")


class FbTest(unittest.TestCase, FbLogin):
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
        time.sleep(5)
        self.assertEqual("Facebook_login", self.driver.title(), "webpage title is not matching")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print(cls.driver.title, "Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
   (output='/Users/user/PycharmProjects/Behave/Behave_Framework/Reports'))