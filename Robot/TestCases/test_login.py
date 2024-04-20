import pytest

from TestCases.TestBase import Test_Base
from Pages.login import login_page


class TestLogin(Test_Base):

    def test_login(self):
        self.login = login_page(self.driver)
        self.login.login_meth()

