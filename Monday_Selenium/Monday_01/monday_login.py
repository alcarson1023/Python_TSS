from selenium.webdriver.common.keys import Keys

from selenium_driver import get_driver
# from misc_helper import send_result

class Monday_Login:
    def __init__(self):
        self.driver = get_driver()

    def monday_login(self, username, monday_password):
        try:
            self.driver.get("https://solartrismart.monday.com/boards/3082655983")

            # Find the username and password fields on the login page
            username_field = self.driver.find_element("id", "user_email")
            password_field = self.driver.find_element("id", "user_password")

            # Enter the username and password in the login fields
            username_field.send_keys(username)
            password_field.send_keys(monday_password)

            # Submit the login form
            password_field.send_keys(Keys.RETURN)
            return ('Successfully logged in...')

        except:
            return ('Something went wrong in the login process.')
