from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage

class ReportsRegistryPage(BasePage):

    SEARCH_INPUT         = (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[2]/input[1]')
    RESULTS_TABLE        = (By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[3]/div[1]/table')
    TABLE_ROWS           = (By.TAG_NAME, 'tr')
    CREATE_REPORT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/button')
    COLUMN_XPATH_TEMPLATE = '/html/body/div[1]/div/div[1]/div[3]/div/div[2]/input[{}]'

    def open_reports_registry(self):
        self.open_url("https://esep.govtec.kz/admin/reports/registry")

    def search_in_registry(self, search_value, column_index=2):
        self.open_reports_registry()

        self.enter_text(self.SEARCH_INPUT, search_value)

        column_xpath = self.COLUMN_XPATH_TEMPLATE.format(column_index)
        checkbox_locator = (By.XPATH, column_xpath)
        checkbox_elem = self.wait_for_element_visible(checkbox_locator)

        if not checkbox_elem.is_selected():
            checkbox_elem.click()

        self.wait_for_element_visible(self.RESULTS_TABLE)

        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*self.TABLE_ROWS)) > 1
        )

        table_rows = self.driver.find_elements(*self.TABLE_ROWS)[1:]
        row_texts = []
        for row in table_rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            row_data = [cell.text for cell in cells]
            row_texts.append(row_data)

        return row_texts

    def create_report_base(self, report_base_id, report_base_name_rus, report_base_name_kaz):
        self.click_element(self.CREATE_REPORT_BUTTON)

        REPORT_BASE_ID_INPUT       = (By.XPATH, '//*[@id="modal-root"]/div/div/div[2]/div[1]/div[2]/input')
        REPORT_BASE_NAME_RUS_INPUT = (By.XPATH, '//*[@id="modal-root"]/div/div/div[2]/div[2]/div[2]/input')
        REPORT_BASE_NAME_KAZ_INPUT = (By.XPATH, '//*[@id="modal-root"]/div/div/div[2]/div[3]/div[2]/input')
        SUBMIT_BUTTON              = (By.XPATH, '//*[@id="modal-root"]/div/div/div[3]/button[1]')

        self.enter_text(REPORT_BASE_ID_INPUT, report_base_id)
        self.enter_text(REPORT_BASE_NAME_RUS_INPUT, report_base_name_rus)
        self.enter_text(REPORT_BASE_NAME_KAZ_INPUT, report_base_name_kaz)

        self.click_element(SUBMIT_BUTTON)
        return self.get_current_url()
