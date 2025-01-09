from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

def select_multiple_dropdowns(driver, dropdowns):

    try:
        for dropdown in dropdowns:
            select_xpath = dropdown["select_xpath"]
            option_text = dropdown["option_text"]

            try:
                dropdown_element = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=(TimeoutException,)).until(
                    EC.element_to_be_clickable((By.XPATH, select_xpath))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_element)
                dropdown_element.click()

                options_container = WebDriverWait(driver, 10, poll_frequency=0.5, ignored_exceptions=(TimeoutException,)).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'sc-ixGGxD')]"))
                )

                for option in options_container:
                    if option.text.strip() == option_text:
                        option.click()
                        break

            except Exception as e:
                print(f"Error while handling dropdown at '{select_xpath}': {e}")

    except Exception as e:
        print(f"An error occurred while handling multiple dropdowns: {e}")


def select_dropdown_option(driver, select_xpath, parent_xpath, option_text):

    try:
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, select_xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()

        dropdown_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, parent_xpath))
        )

        WebDriverWait(driver, 5).until(EC.visibility_of(dropdown_container))

        options = dropdown_container.find_elements(By.XPATH, ".//div")

        for option in options:
            if option.text.strip() == option_text:
                option.click()
                return True
        else:
            print(f"Option '{option_text}' not found in the dropdown!")
            return False

    except Exception as e:
        print(f"An error occurred while selecting the dropdown option: {e}")
        return False


def fill_input_with_value(driver, input_xpath, value):

    try:
        input_elem = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, input_xpath))
        )
        input_elem.clear()
        input_elem.send_keys(value)
    except Exception as e:
        print(f"An error occurred while filling input: {e}")
