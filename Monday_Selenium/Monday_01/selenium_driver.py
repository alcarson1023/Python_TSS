from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create a global variable to store the driver instance
driver = None

# Define a function to get the driver instance
def get_driver():
    global driver
    if not driver:
        driver = webdriver.Chrome(ChromeDriverManager().install())
# Dimensions are 1920 & 1080, both scaled down by 10%.
        driver.set_window_size(1728, 972)
    return driver
