from selenium.webdriver.common.by import By


class HomePage:
    home_page_menu_xpath = "//*[@id='react-burger-menu-btn']"
    logout_button = "logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def click_main_menu(self):
        self.driver.find_element(By.XPATH, self.home_page_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.ID, self.logout_button).click()

    def get_text(self):
        booltext = self.driver.find_element(By.XPATH, self.home_page_menu_xpath).is_displayed()
        return booltext
