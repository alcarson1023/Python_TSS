from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from selenium_driver import get_driver

class Smarboard_Message_Contact:
    def monday_add_user(self, fullName, address, phone, email, submittedDate, source):
        self.driver = get_driver()

        class Actions:

            def send_keys(self, keys):
                ActionChains(self.driver).send_keys(keys).perform()

            def __init__(self, xpath):
                self.xpath = xpath
            def delay_click(self, xpath):
                self.driver = get_driver()
                loadingDiv = 'unLoaded'
                # Adding this chunk so we can display an error if the system gets stuck for too long.
                attempts = 0
                if(attempts < 50):
                    while loadingDiv == 'unLoaded':
                        try:
                            self.driver.find_element("xpath", xpath).click()
                            loadingDiv = 'loaded'
                        except:
                            attempts += 1
                            time.sleep(.5)
                            pass
                else:
                    print('delay_click failed while adding a user.')

        actions = Actions('placeholder')

        actions.delay_click(
            '//*[@id="board-header-view-bar"]/div/div[2]/div/div[1]/button')

        time.sleep(1)
        actions.send_keys(str(fullName))
        time.sleep(0.25)
        actions.send_keys(Keys.TAB)
        time.sleep(0.25)
        actions.send_keys(Keys.TAB)
        time.sleep(0.25)
        actions.send_keys(Keys.TAB)
        time.sleep(0.25)
        actions.send_keys(Keys.TAB)
        time.sleep(0.25)
        actions.send_keys(Keys.RETURN)
        time.sleep(0.75)
        actions.send_keys(str(source))
        time.sleep(0.25)
        actions.send_keys(Keys.RETURN)
        time.sleep(0.25)
        actions.send_keys(Keys.ESCAPE)
        time.sleep(0.25)
        actions.send_keys(Keys.TAB)
        time.sleep(0.25)
        actions.send_keys(Keys.RETURN)
        time.sleep(0.75)
        actions.send_keys(str(phone))
        time.sleep(0.25)
        actions.send_keys(Keys.TAB)
        time.sleep(0.25)
        actions.send_keys(Keys.TAB)
        time.sleep(0.25)
        actions.send_keys(Keys.RETURN)
        time.sleep(0.75)
        actions.send_keys(str(email))
        time.sleep(0.25)
        actions.send_keys(Keys.RETURN)
        time.sleep(0.25)
        actions.send_keys(Keys.TAB)
        time.sleep(0.25)
        actions.send_keys(Keys.RETURN)
        time.sleep(0.75)
        actions.send_keys(str(address))
        time.sleep(0.25)
        actions.send_keys(Keys.RETURN)

# Look for "No results found". If it's not there after a few seconds, continue with the process.
# UPDATE THIS WITH SOMETHING FASTER SOON. Something less dependent on load times, as well. If we find the entered name, break out of the process. If we find "No results", carry on.
        time.sleep(1.5)

# Try to find the image that appears when no results are found. If the attempt fails, that means there's at least one result.0
        try:
            self.driver.find_element("xpath", '//*[@id="board-content-component_currentBoard"]/div/div/div/img')
            # Reload the page, because escaping the search bar is a hassle.
            self.driver.get('https://solartrismart.monday.com/boards/3082655983')
            return ('No users with matching numbers found...')
        except:
            return (f'Number {phone} already exists.')