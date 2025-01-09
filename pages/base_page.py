
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def enter_text(self, locator, text, clear_first=True):

        element = self.wait_for_element_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url
