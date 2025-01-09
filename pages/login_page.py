
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    USERNAME_FIELD = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div[2]/div[2]/input')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div[3]/div[2]/input')
    LOGIN_BUTTON   = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/button[1]')

    def open_login_page(self):
        self.open_url("https://esep.govtec.kz/login")

    def login(self, username, password, success_url):
        self.open_login_page()
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)

        WebDriverWait(self.driver, 10).until(
            lambda driver: self.get_current_url() == success_url
        )

        current_url = self.get_current_url()
        if current_url != success_url:
            raise Exception(f"Login failed or did not redirect to the expected URL. Current URL: {current_url}")
        
        return self.get_current_url()
