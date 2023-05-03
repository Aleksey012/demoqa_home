from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo').click()
        except NoSuchElementException:
            return False
        return True

    def get_url(self):
        if self.get_url('https://www.saucedemo.com/'):
            return True
        return False


    def user_name(self):

        try:
            self.find_element(locator='#user-name').click()
        except NoSuchElementException:
            return False
        return True


    def password(self):

        try:
            self.find_element(locator='#password').click()
        except NoSuchElementException:
            return False
        return True
