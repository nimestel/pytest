from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        self.wd.get("http://addressbook/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
