
import pytest
from utils.driver_factory import init_driver
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_url", [
    ("invalid_user", "invalid_pass", "https://esep.govtec.kz/login"),
    ("edugov", "Fnj0K8Ge", "https://esep.govtec.kz/participant"),
    ("edugov_admin", "CuShF33o", "https://esep.govtec.kz/admin"),
])
def test_login(username, password, expected_url):
    driver = init_driver()
    login_page = LoginPage(driver)

    current_url = login_page.login(username, password, expected_url)



    assert expected_url in current_url, f"Expected '{expected_url}' to be part of '{current_url}'"

    driver.quit()