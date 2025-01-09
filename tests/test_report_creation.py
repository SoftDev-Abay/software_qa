
import pytest
from utils.driver_factory import init_driver
from pages.login_page import LoginPage
from pages.reports_registry_page import ReportsRegistryPage
from pages.template_editor_page import TemplateEditorPage

def test_create_report_and_template():


    driver = init_driver()
    login_page = LoginPage(driver)
    registry_page = ReportsRegistryPage(driver)
    template_editor = TemplateEditorPage(driver)

    login_page.login("edugov_admin", "CuShF33o", "https://esep.govtec.kz/admin")

    registry_page.open_reports_registry()

    report_base_id = "testing_qa11"
    report_base_name_rus = "Тестовый отчет"
    report_base_name_kaz = "Сынақ есеп"

    current_url = registry_page.create_report_base(report_base_id, report_base_name_rus, report_base_name_kaz)
    print(f"Created new report base, current URL: {current_url}")


    template_id = "testing_qa11"
    template_editor.open_template_editor(template_id)

    table_name = "Table1"
    template_editor.create_table(table_name, is_static=True, row_count=5, col_count=4)
    print("Table created in template editor.")

    template_editor.save_template()
    print("Template saved successfully.")

    driver.quit()
