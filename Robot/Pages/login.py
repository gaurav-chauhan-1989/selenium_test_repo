
import time

from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from Config.TestData import Test_Data
from Pages.BasePage import Base_Page

class login_page(Base_Page):

    name = (By.ID, "name")
    email = (By.ID, "email")
    phone = (By.ID, "phone")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Test_Data.url)
        self.driver.maximize_window()

    def login_meth(self):
        self.set_text(self.name, "Gaurav")
        time.sleep(5)
        self.set_text(self.email, "chauhan.gaurav4@gmail.com")
        time.sleep(5)
        self.set_text(self.phone, "9811597772")
        time.sleep(5)