from selenium import webdriver
import unittest
import sys
import time
import HtmlTestRunner

driver = webdriver.Chrome(executable_path="/Users/user/Desktop/chromedriver")
driver.get("http://wwww.facebook.com")
