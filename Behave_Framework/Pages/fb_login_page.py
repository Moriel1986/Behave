

class FbLogin:

    username_xpath = "//input[@id='email']"
    password_xpath = "//input[@id='pass']"
    click_login_id = "//input[@id='u_0_4']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_xpath(self.username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(self.click_login_id).click()



