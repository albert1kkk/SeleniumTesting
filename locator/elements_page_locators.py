from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[name='text-928']")
    EMAIL = (By.CSS_SELECTOR, "input[name='email-845']")
    PHONE = (By.CSS_SELECTOR, "input[name='text-847']")
    HEADER = (By.XPATH, "//*[@id=\"wpcf7-f598-p584-o1\"]/form/p[1]/span[4]/input")
    MASSAGE = (By.CSS_SELECTOR, "textarea[name='textarea-595']")


class RegistrationBox:

    RegistrationButton = (By.XPATH, "/html/body/header/nav/a[2]")
    RegistrationButton2 = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/header/div/div/a[2]")
    FirstName_SecondName = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/form/div[1]/input[1]")
    Mail = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/form/div[1]/input[2]")
    Password = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/form/div[1]/input[3]")
    Button = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/form/button")


class LoginBox:

    LoginButton = (By.XPATH, "/html/body/header/nav/a[2]")
    EMAIL = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/input[1]")
    PASSWORD = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/input[2]")
    LoginButton2 = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/button")

class SearchStepik:

    SearchButton = (By.XPATH, "/html/body/header/nav/form/div/span/div/div/div/div/input")
    Like = (By.XPATH, "/html/body/main/div[1]/div[2]/div/div[1]/ul/li[1]/div/button/span")
