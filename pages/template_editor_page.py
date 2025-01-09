
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TemplateEditorPage(BasePage):


    CREATE_TABLE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div/div/div/button[1]')
    SAVE_TEMPLATE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div/div/div[1]/button[2]')

    TABLE_NAME_INPUT = (By.CSS_SELECTOR, "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div:nth-child(1) > div > input[type='text']")
    STATIC_BUTTON     = (By.CSS_SELECTOR, "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-i9qltj > div:nth-child(1) > div")
    DYNAMIC_BUTTON    = (By.CSS_SELECTOR, "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-i9qltj > div:nth-child(2) > div")
    ROW_COUNT_INPUT   = (By.CSS_SELECTOR, "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.body-footer > div:nth-child(1) > div > input[type=number]")
    COL_COUNT_INPUT   = (By.CSS_SELECTOR, "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.body-footer > div:nth-child(2) > div > input[type=number]")
    SUBMIT_TABLE_BTN  = (By.CSS_SELECTOR, "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-footer > button:nth-child(2)")

    def open_template_editor(self, template_id):
        url = f"https://esep.govtec.kz/admin/reports/templateEditor/{template_id}"
        self.open_url(url)

    def create_table(self, table_name, is_static=True, row_count=5, col_count=4):
        self.click_element(self.CREATE_TABLE_BUTTON)

        self.enter_text(self.TABLE_NAME_INPUT, table_name)

        if is_static:
            self.click_element(self.STATIC_BUTTON)
        else:
            self.click_element(self.DYNAMIC_BUTTON)

        self.enter_text(self.ROW_COUNT_INPUT, str(row_count))
        self.enter_text(self.COL_COUNT_INPUT, str(col_count))

        self.click_element(self.SUBMIT_TABLE_BTN)

    def save_template(self):
        self.click_element(self.SAVE_TEMPLATE_BUTTON)
