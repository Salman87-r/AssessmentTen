from selenium.webdriver.common.by import By


class LoginPage:
    username_textbox_id = "user-name"
    password_textbox_id = "password"
    login_button_id = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def set_user_name(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def set_user_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

    def check_login_button(self):
        loginBtn = self.driver.find_element(By.ID, self.login_button_id).is_displayed()
        return loginBtn
