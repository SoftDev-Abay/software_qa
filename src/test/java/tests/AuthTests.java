package tests;

import com.aventstack.extentreports.ExtentTest;
import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import pages.LoginPage;

public class AuthTests extends BaseTest {

    @DataProvider(name = "loginData")
    public Object[][] loginData() {
        return new Object[][] {
                {"invalid_user", "invalid_pass", "https://esep.govtec.kz/login"},
                {"edugov",       "Fnj0K8Ge",     "https://esep.govtec.kz/participant"},
                {"edugov_admin", "CuShF33o",     "https://esep.govtec.kz/admin"}
        };
    }

    @Test(dataProvider = "loginData")
    public void testLogin(String username, String password, String expectedUrl) {
        extentTest = extentReports.createTest("testLogin: " + username);
         logger.info("Starting login test for user: " + username);

        try {
            LoginPage loginPage = new LoginPage(driver);
            loginPage.login(username, password, expectedUrl);

            String currentUrl = driver.getCurrentUrl();
            extentTest.info("Current URL after login: " + currentUrl);

            Assert.assertTrue(
                    currentUrl.contains(expectedUrl),
                    "Expected URL to contain: " + expectedUrl + " but got: " + currentUrl
            );
            extentTest.pass("Login test passed for user: " + username);

        } catch (Exception e) {
            extentTest.fail("Login test failed for user: " + username + "\n" + e.getMessage());
             logger.error("Exception during login test: ", e);
            Assert.fail(e.getMessage());
        }
    }
}
