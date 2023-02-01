from pages.base_page import BasePage
import time

def test(get_webdriver):
    page = BasePage(get_webdriver, "https://test.qa.studio/contact-us/")
    page.open()
    time.sleep(5)