from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_multiple_dropdowns(driver, dropdowns):
    """
    Logs in, navigates to the target URL, and tests interaction with multiple dynamically rendered dropdowns.

    Args:
        driver: Selenium WebDriver instance.
        dropdowns: A list of dictionaries containing dropdown and option details.
    """
    try:

        # Step 3: Handle all dropdowns
        for dropdown in dropdowns:
            select_xpath = dropdown["select_xpath"]
            option_text = dropdown["option_text"]

            try:
                # Click the dropdown
                dropdown_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, select_xpath))
                )
                dropdown_element.click()
                print(f"Dropdown at '{select_xpath}' clicked.")

                # Wait for the dropdown options and select the desired one
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'sc-ixGGxD')]"))
                )
                print("Dropdown options container detected.")

                options = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-ixGGxD')]")
                print(f"Found {len(options)} options in the dropdown.")

                for option in options:
                    print(f"Checking option: {option.text.strip()}")
                    if option.text.strip() == option_text:
                        option.click()
                        print(f"Option '{option_text}' selected successfully.")
                        break
                else:
                    print(f"Option '{option_text}' not found in the dropdown.")

            except Exception as e:
                print(f"Error while handling dropdown at '{select_xpath}': {e}")

    except Exception as e:
        print(f"An error occurred while testing the dropdowns: {e}")



def select_dropdown_option(driver, select_xpath, parent_xpath, option_text):
    """
    Selects a specific dropdown option based on visible text in an MUI dropdown.

    Args:
        driver: Selenium WebDriver instance.
        select_xpath: XPath of the dropdown element.
        parent_xpath: XPath of the parent container of dropdown options.
        option_text: The text of the option to select.
    """
    try:
        # Locate and click the dropdown
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, select_xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()
        print(f"Dropdown at '{select_xpath}' clicked.")

        # Wait for the dropdown options to appear
        dropdown_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, parent_xpath))
        )
        print(f"Dropdown container found at '{parent_xpath}'.")

        # Wait for visibility
        WebDriverWait(driver, 5).until(EC.visibility_of(dropdown_container))

        # Locate options dynamically
        options = dropdown_container.find_elements(By.XPATH, ".//div")
        print(f"Found {len(options)} options in the dropdown.")

        # Iterate and select the correct option
        for option in options:
            print(f"Option found: '{option.text.strip()}'")
            if option.text.strip() == option_text:
                option.click()
                print(f"Option '{option_text}' selected successfully.")
                return True
        else:
            print(f"Option '{option_text}' not found in the dropdown!")

    except Exception as e:
        print(f"An error occurred while selecting the dropdown option: {e}")
        return False


def fill_input_with_value(driver, input_xpath, value):
    try:
        template_id_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, input_xpath))
        )
        template_id_input.send_keys(value)

        print(f"Input filled with '{value}' successfully.")
    except Exception as e:
        print(f"An error occurred while selecting the dropdown option: {e}")



