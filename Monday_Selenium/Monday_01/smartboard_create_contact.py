from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from selenium_driver import get_driver

class Smartboard_Create_Contact:
    # def smartboard_create_contact(self, username, monday_password, smartboard_password, fullName, address, phone, email, source, confirmation):
    def smartboard_create_contact(self, username, smartboard_password, fullName, phone, email, confirmation):
        self.driver = get_driver()

        class Actions:

            def __init__(self, driver, xpath):
                self.driver = driver
                self.xpath = xpath

            def send_keys(self, keys):
                ActionChains(self.driver).send_keys(keys).perform()

            def delay_click(self, xpath):
                self.driver = get_driver()
                loadingDiv = 'unLoaded'
                # Adding this chunk so we can display an error if the system gets stuck for too long. 50 second wait time, so the user can enter the security code.
                attempts = 0
                if(attempts < 100):
                    while loadingDiv == 'unLoaded':
                        try:
                            self.driver.find_element("xpath", xpath).click()
                            loadingDiv = 'loaded'
                        except:
                            attempts += 1
                            time.sleep(.5)
                            pass
                else:
                    return('delay_click took too long in SB_Create_Contact.')

        actions = Actions(self.driver, 'placeholder')

        
        self.driver.get('https://app.smartboardcrm.com/')

        try:
    # This code gets us through the login screen. First line is designed to break it if we're not on the login screen.
            time.sleep(1.5)
            self.driver.find_element("xpath", "//*[text() = 'Sign into your account']").click()
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(str(username))
            time.sleep(0.25)
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(str(smartboard_password))
            time.sleep(0.25)
            actions.send_keys(Keys.ENTER)
            
    # This will trigger the security code being sent out.
            if('Email' not in confirmation):
                print('Sending a text message.')
                actions.delay_click(
                    "//*[text() = ' Send code to phone ']")

            print('Attempting to send the code.')
            actions.delay_click(
                "//*[text() = ' Send Security Code']")
            
        except:
            print('Already logged in.')

        try:

    # This code opens the module to create a contact.
            print('Looking for "Contacts"')
            actions.delay_click(
                '//*[@id="sb_contacts"]/img')
            
            actions.delay_click(
                '//*[@id="smartlists"]/div[2]/div[1]/span[1]/button/i')

    # This code enters the contact information.
            split_name = fullName.split(" ")
            first_name = split_name[0]
            last_name = ' '.join(split_name[1::])

            time.sleep(1.5)
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(str(first_name))
            time.sleep(0.25)
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(str(last_name))
            time.sleep(0.25)
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(str(email))
            time.sleep(0.25)
            actions.send_keys(Keys.TAB)
            time.sleep(0.25)
            actions.send_keys(str(phone))

            # This is where I'll add code to click on the "Save" button, when the script is deemed ready.

            return('The contact has been added to Monday & SmartBoard!')
        except:
            return('Something went wrong in SB_Create_Contact')
