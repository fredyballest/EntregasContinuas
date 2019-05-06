import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class GrammarlyGeneralTest(unittest.TestCase):

    def setUp(self):
        # for dev I'll use only visible browser instead of no-gui one.
        # but for production, it will use the no-gui one.
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}
        )

    def test_example(self):
        # run tests
       driver.get("http://askubuntu.com")
       print driver.page_source.encode('utf-8')  