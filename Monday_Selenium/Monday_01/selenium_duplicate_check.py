from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
import time

from selenium_driver import get_driver
# from misc_helper import send_result

class Duplicate_Check:
    def duplicate_check(self, phone):
        self.driver = get_driver()

        class Actions:
            def __init__(self, xpath):
                self.xpath = xpath

# Consider bumping this out of Actions and see if it still requires the self.driver line.
            def delay_click(self, xpath):
# Not sure why this is required in this spot, but putting it inside just the class doesn't work. Only inside this function.
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
                            time.sleep(.5)
                            attempts += 1
                            pass
                else:
                    print('Unable to find the search bar.')

        actions = Actions('placeholder')

        actions.delay_click(
            '//*[@id="board-header-view-bar"]/div/div[3]/div[1]/div/div/input')
        ActionChains(self.driver).send_keys(phone).perform()

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