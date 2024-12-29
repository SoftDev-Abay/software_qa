import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

import time



load_dotenv()


# SSL checking
if not hasattr(ssl, '_create_unverified_context'):
    print("SSL module is not properly configured. Ensure your Python environment supports SSL.")


def login_to_application(driver, username, password):
    """
    Utility function to log in to the application.
    Can be reused wherever login functionality is required.
    """
    driver.get("https://esep.govtec.kz/login")  # Navigate to the login page

    try:
        # Wait for the username field to be present and input username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[2]/div[2]/input'))
        )
        username_field.clear()
        username_field.send_keys(username)

        # Wait for the password field to be present and input password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[3]/div[2]/input'))
        )
        password_field.clear()
        password_field.send_keys(password)

        # Wait for the login button to be clickable and then click
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/button[1]'))
        )
        login_button.click()

        # Wait until redirected after a successful login
        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != "https://esep.govtec.kz/login"
        )

        print("Login successful.")
    except Exception as e:
        print(f"Login failed: {e}")
        driver.quit()  # Quit the driver and raise an exception
        raise



def test_login_logout(driver, username, password, expected_url):
    # Navigate to the login page

    driver.get("https://esep.govtec.kz/login")

    try:
        # Wait for the username field to be present
        print("Waiting for username field...")
        username_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div[2]/div[2]/input'))
        )
        username_field.clear()
        username_field.send_keys(username)

        # Wait for the password field to be present
        print("Waiting for password field...")
        password_field = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id=\"root\"]/div/div[1]/div[3]/div/div[3]/div[2]/input'))
        )
        password_field.clear()
        password_field.send_keys(password)

        # Wait for the login button to be clickable
        print("Waiting for login button...")
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id=\"root\"]/div/div[1]/div[3]/div/button[1]'))
        )
        login_button.click()

        # Wait for redirection
        print("Waiting for redirection...")
        WebDriverWait(driver, 20).until(
            lambda d: d.current_url != "https://esep.govtec.kz/login"
        )

        # Check the current URL to validate the login success
        current_url = driver.current_url
        if current_url == expected_url:
            print(f"Login successful for user: {username}")

            # Logout functionality
            print("Logging out...")
            driver.get("https://esep.govtec.kz/login")
            logout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/button[1]'))
            )
            logout_button.click()
            print(f"Logout successful for user: {username}")
        else:
            print(f"Login failed for user: {username}")

    except Exception as e:
        print(f"An error occurred during login/logout: {e}")


def test_search_functionality(driver, search_value, column_xpath, expected_results, username, password):
    # Navigate to the search page
    login_to_application(driver, username, password)

    driver.get("https://esep.govtec.kz/admin/reports/registry")

    try:
        # Wait for the search input to be present
        print("Waiting for search input field...")
        search_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[2]/input[1]'))
        )
        search_input.clear()
        search_input.send_keys(search_value)

        # Wait for the checkbox to be present
        print("Waiting for checkbox...")
        column_checkbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, column_xpath))
        )
        if not column_checkbox.is_selected():
            column_checkbox.click()

        # Trigger the search (if needed, press Enter or locate a Search button)
        print("Triggering search...")
        search_input.send_keys(Keys.RETURN)

        # Wait for the table to update
        print("Waiting for table to update...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[3]/div/div[3]/div[1]/table'))
        )

        # Collect the results from the table
        print("Collecting results...")
        # Find all <tr> tags inside <tbody>
        rows = driver.find_elements(By.TAG_NAME, 'tr')
        rows = rows[1:]  # Skip the first row

        print(f"Number of rows found: {len(rows)}")

        results = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')

            results.append([cell.text for cell in cells])

        # print('results: ', results)

        # Validate the results
        print("Validating results...")
        for result, expected in zip(results, expected_results):
            if result[:2] != expected:
                print(f"Search test failed. Expected: {expected}, Got: {result[:2]}")
            else:
                print(f"Search test passed for: {expected}")

    except Exception as e:
        print(f"An error occurred during the search test: {e}")


def test_create_report_template(driver, username, password, report_base_id, report_base_name_rus, report_base_name_kaz,
                                template_id, template_name_rus, template_name_kaz, table_name, is_static, row_count,
                                col_count):
    login_to_application(driver, username, password)

    # go the page of registry
    driver.get("https://esep.govtec.kz/admin/reports/registry")

    # createing a report base
    try:
        create_report_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/button'))
        )
        create_report_button.click()

        # fill the modal inputs
        report_base_id_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root"]/div/div/div[2]/div[1]/div[2]/input'))
        )
        report_base_id_input.send_keys(report_base_id)

        report_base_name_rus_input = driver.find_element(By.XPATH,
                                                         '//*[@id="modal-root"]/div/div/div[2]/div[2]/div[2]/input')
        report_base_name_rus_input.send_keys(report_base_name_rus)

        report_base_name_kaz_input = driver.find_element(By.XPATH,
                                                         '//*[@id="modal-root"]/div/div/div[2]/div[3]/div[2]/input')
        report_base_name_kaz_input.send_keys(report_base_name_kaz)

        submit_button = driver.find_element(By.XPATH, '//*[@id="modal-root"]/div/div/div[3]/button[1]')
        submit_button.click()

        print("Report base creation submitted.")

    except Exception as e:
        print(f"Failed to create report base: {e}")
        driver.quit()
        raise

    # createing a report template
    try:
        driver.get("https://esep.govtec.kz/admin/reports/info/" + report_base_id)

        report_template_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div[1]/div[2]'))
        )
        report_template_tab.click()

        create_template_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div[2]/div/button'))
        )
        create_template_button.click()

        # again fill the modal inputs
        template_id_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="modal-root"]/div/div/div[2]/div[1]/div[2]/input'))
        )
        template_id_input.send_keys(template_id)

        template_name_rus_input = driver.find_element(By.XPATH,
                                                      '//*[@id="modal-root"]/div/div/div[2]/div[2]/div[2]/input')
        template_name_rus_input.send_keys(template_name_rus)

        template_name_kaz_input = driver.find_element(By.XPATH,
                                                      '//*[@id="modal-root"]/div/div/div[2]/div[3]/div[2]/input')
        template_name_kaz_input.send_keys(template_name_kaz)

        submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button[1]')
        submit_button.click()

        print("Report template creation submitted.")

        # verifing template creation
        template_editor_url = f"https://esep.govtec.kz/admin/reports/templateEditor/{template_id}"
        driver.get(template_editor_url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div/div/div/button[1]'))
            )
            print("Report template created successfully.")
        except Exception:
            print("Report template not found. Creation might have failed.")
            driver.quit()
            raise

    except Exception as e:
        print(f"Failed to create report template: {e}")
        driver.quit()
        raise

    # configure table in the template table
    try:
        table_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div/div/div/button[1]'))
        )
        table_button.click()

        print('table create model opened. ' )

        table_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div:nth-child(1) > div > input[type='text']"))
        )

        if table_name_input:
            print('table_name_input found: ', table_name_input)
        else:
            print('table_name_input not found: ', table_name_input)


        if table_name_input : table_name_input.send_keys(table_name)

        if is_static:
            static_button = driver.find_element(By.CSS_SELECTOR,
                                            "body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-i9qltj > div:nth-child(1) > div")
            static_button.click()
        else:
            dynamic_button = driver.find_element(By.CSS_SELECTOR, 'body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-i9qltj > div:nth-child(2) > div')
            dynamic_button.click()

        row_count_input = driver.find_element(By.CSS_SELECTOR, 'body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.body-footer > div:nth-child(1) > div > input[type=number]')
        row_count_input.send_keys(row_count)

        col_count_input = driver.find_element(By.CSS_SELECTOR, 'body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.body-footer > div:nth-child(2) > div > input[type=number]')
        col_count_input.send_keys(col_count)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-footer > button:nth-child(2)')
        submit_button.click()

        print("Table created successfully.")

        # saving the template
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/div/div/div/div/div/div[1]/button[2]'))
        )
        save_button.click()
        print("Template saved successfully.")

    except Exception as e:
        print(f"Failed to configure table: {e}")
        driver.quit()
        raise


def initialize_driver():
    try:
        driver = webdriver.Chrome()  # You can use a different driver like Firefox or Edge
        return driver
    except Exception as e:
        print(f"WebDriver initialization failed: {e}")
        return None


test_data = [
    {
        "username": os.getenv("USERNAME_INVALID"),
        "password": os.getenv("PASSWORD_INVALID"),
        "expected_url": os.getenv("EXPECTED_URL_INVALID"),
    },
    {
        "username": os.getenv("USERNAME_PARTICIPANT"),
        "password": os.getenv("PASSWORD_PARTICIPANT"),
        "expected_url": os.getenv("EXPECTED_URL_PARTICIPANT"),
    },
    {
        "username": os.getenv("USERNAME_ADMIN"),
        "password": os.getenv("PASSWORD_ADMIN"),
        "expected_url": os.getenv("EXPECTED_URL_ADMIN"),
    },
]


search_test_data = [
    {
        "search_value": "04001",
        "column_xpath": '//*[@id="root"]/div/div[1]/div[3]/div/div[2]/input[2]',
        "expected_results": [
            ["040010",
             "Д-9 раздел I. Сведения о специальных организациях образования и численности школ, школ-интернатов, учителей, учащихся"],
            ["040011", "Д-9 (раздел II). Сведения о распределении учащихся по классам"],
            ["040012", "Д-9 (раздел III). Сведения о материальной базе специальных организаций образования"],
            ["040013", "МКШ-1. Сеть и контингент малокомплектных школ (МКШ)"],
            ["040014",
             "МКШ-2. Сведения о совмещенных классах и контингенте обучающихся в малокомплектных школах и количество школ по числу учащихся"],
            ["040015", "МКШ-3. Сведения о малокомплектных школах по языкам обучения, по классам"],
            ["040016", "МКШ-4. Сведения о материальной базе малокомплектных школ"],
            ["040017", "МКШ-6. Сведения о качественном составе педагогических кадров малокомплектных школ"],
            ["040018", "МКШ-10. Сеть ресурсных центров"],
            ["040019", "СТ-1. Отчет об основных показателях среднего образования"]
        ]
    },
    {
        "search_value": "дошкольных",
        "column_xpath": '/html/body/div[1]/div/div[1]/div[3]/div/div[2]/input[3]',
        "expected_results": [
            ["040001", "ДО-1. Сведения о сети и контингенте детей дошкольных организаций"],
            ["040002",
             "ДО-2. Сведения о сети и контингенте детей в дошкольных организациях за исключением мини-центров"],
            ["040073", "ДО-4. Сведения о дошкольных организациях (группах) по языкам обучения"],
            ["040075", "ДО-7. Сведения о качественном составе педагогических кадров дошкольных организаций"],
            ["040076",
             "ДО-8. Сведения о сети и контингенте дошкольных организаций негосударственной формы собственности"],
            ["040077", "ДО-9. Сведения о материальной базе дошкольных организаций"],
            ["040078", "ДО-11. Сведения о специальных дошкольных организациях и о педагогическом составе"],
            ["040080", "ДО-13. Сведения о сети и контингенте в дошкольных организациях за исключением детских садов"],
            ["040082", "ДО-15. Сведения о мониторинге открытия и закрытия дошкольных организаций"]
        ]
    }

]


# tests
def main():
    driver = initialize_driver()
    if driver is None:
        print("WebDriver could not be initialized. Exiting the program.")
        return

    # login/logout tests
    for data in test_data:
        test_login_logout(driver, data["username"], data["password"], data["expected_url"])

    # search tests (admin login required)
    for search_data in search_test_data:
        test_search_functionality(driver, search_data["search_value"], search_data["column_xpath"],
                                  search_data["expected_results"], test_data[2]['username'], test_data[2]['password'])

    test_create_report_template(
        driver,
        username=os.getenv("USERNAME_ADMIN"),
        password=os.getenv("PASSWORD_ADMIN"),
        report_base_id="testing_qa4",
        report_base_name_rus="Тестовый отчет",
        report_base_name_kaz="Сынақ есеп",
        template_id="testing_qa4",
        template_name_rus="Шаблон отчета",
        template_name_kaz="Есеп үлгісі",
        table_name="Table1",
        is_static=True,
        row_count="5",
        col_count="4"
    )

    driver.quit()


if __name__ == "__main__":
    main()
