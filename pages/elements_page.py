from locator.elements_page_locators import TextBoxPageLocators
from locator.elements_page_locators import RegistrationBox
from locator.elements_page_locators import LoginBox
from locator.elements_page_locators import SearchStepik
from pages.base_page import BasePage
import time


# class TextBoxPage(BasePage): "Отдеальная проверка другого сайта"
#     locators = TextBoxPageLocators()
#
#     def fill_all_fields(self):
#         self.element_is_visible(self.locators.FULL_NAME).send_keys("YourName")
#         self.element_is_visible(self.locators.EMAIL).send_keys("yourmail@mail.ru")
#         self.element_is_visible(self.locators.PHONE).send_keys("+7934588775")
#         self.element_is_visible(self.locators.HEADER).send_keys("Здесь будет текст заголовка")
#         self.element_is_visible(self.locators.MASSAGE).send_keys("А здесь будет текст сообщения")
#         time.sleep(5)


class RegistrationBoxPage(BasePage):
    locators = RegistrationBox()

    def fill_registration_fields(self):
        self.element_is_visible(self.locators.RegistrationButton).click()
        self.element_is_visible(self.locators.RegistrationButton2).click()
        self.element_is_visible(self.locators.FirstName_SecondName).send_keys("Имя Фамилия")
        self.element_is_visible(self.locators.Mail).send_keys("ivibesplatno1@rambler.ru")
        self.element_is_visible(self.locators.Password).send_keys("12345678!A")
        self.element_is_visible(self.locators.Button).click()


class LoginBoxPage(BasePage):
    locators = LoginBox()

    def fill_login_fields(self):
        self.element_is_visible(self.locators.LoginButton).click()
        self.element_is_visible(self.locators.EMAIL).send_keys("ivibesplatno1@rambler.ru")
        self.element_is_visible(self.locators.PASSWORD).send_keys("12345678!A")
        self.element_is_visible(self.locators.LoginButton2).click()


class SearchBoxPage(BasePage):
    locators = SearchStepik

    def fill_search_bar(self):
        self.element_is_visible(self.locators.SearchButton).click()
        self.element_is_visible(self.locators.SearchButton).send_keys("Python \n")
        self.element_is_visible(self.locators.Like).click()
