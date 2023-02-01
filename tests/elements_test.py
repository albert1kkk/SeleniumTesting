import time
from pages.elements_page import TextBoxPage
from pages.elements_page import RegistrationBoxPage
from pages.elements_page import LoginBoxPage
from pages.elements_page import SearchBoxPage


class TestElements:
    class TestBoxes:

        # def test_text_box(self, get_webdriver):
        #     test_box_page = TextBoxPage(get_webdriver, "https://test.qa.studio/contact-us/")
        #     test_box_page.open()
        #     test_box_page.fill_all_fields()
        #     time.sleep(3)


        def test_reg_box(self, get_webdriver):
            test_registration_box = RegistrationBoxPage(get_webdriver, "https://stepik.org/catalog")
            test_registration_box.open()
            test_registration_box.fill_registration_fields()
            time.sleep(3)


        def test_log_box(self, get_webdriver):
            test_login_box = LoginBoxPage(get_webdriver, "https://stepik.org/catalog")
            test_login_box.open()
            test_login_box.fill_login_fields()
            time.sleep(3)


        def test_search_box(self, get_webdriver):
            test_search_box = SearchBoxPage(get_webdriver, "https://stepik.org/catalog")
            test_search_box.open()
            test_search_box.fill_search_bar()
            time.sleep(5)
