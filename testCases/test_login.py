import time
from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage


class Test_001_Login:
    baseURL = "https://www.saucedemo.com/"
    validUserName = "standard_user"
    validUserPassword = "secret_sauce"
    invalidUserName = "standard_u"
    invalidUserPassword = "secret_sauc"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        title = self.driver.title
        if title == 'Swag Labs':
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./ScreenShots/" + "test_homePageTitle")
            self.driver.close()
            assert False

    def test_loginAppSuccessfully(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.validUserName)
        self.lp.set_user_password(self.validUserPassword)
        self.lp.click_login_button()
        self.hp = HomePage(self.driver)
        time.sleep(10)
        title = self.hp.get_text()
        if title == True:
            self.hp.click_main_menu()
            self.hp.click_logout()
            self.driver.close()
            assert True
        else:
            self.hp.click_main_menu()
            self.hp.click_logout()
            self.driver.save_screenshot("./ScreenShots/" + "test_loginAppSuccessfully")
            self.driver.close()
            assert False

    def test_inValidCred(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.invalidUserName)
        self.lp.set_user_password(self.invalidUserPassword)
        self.lp.click_login_button()
        checkLoginPage = self.lp.check_login_button()
        if checkLoginPage:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./ScreenShots/" + "test_inValidCred")
            self.driver.close()
            assert False

    def test_invalidPassword(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.validUserName)
        self.lp.set_user_password(self.invalidUserPassword)
        self.lp.click_login_button()
        checkLoginPage = self.lp.check_login_button()
        if checkLoginPage:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./ScreenShots/" + "test_invalidPassword")
            self.driver.close()
            assert False

    def test_invalidUserName(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_user_name(self.invalidUserName)
        self.lp.set_user_password(self.validUserPassword)
        self.lp.click_login_button()
        checkLoginPage = self.lp.check_login_button()
        if checkLoginPage:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("./ScreenShots/" + "test_invalidUserName")
            self.driver.close()
            assert False
