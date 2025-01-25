package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import java.time.Duration;

public class LoginPage extends BasePage {

    private final By USERNAME_FIELD = By.xpath("//*[@id=\"root\"]/div/div[1]/div[3]/div/div[2]/div[2]/input");
    private final By PASSWORD_FIELD = By.xpath("//*[@id=\"root\"]/div/div[1]/div[3]/div/div[3]/div[2]/input");
    private final By LOGIN_BUTTON   = By.xpath("//*[@id=\"root\"]/div/div[1]/div[3]/div/button[1]");

    public LoginPage(WebDriver driver) {
        super(driver);
    }

    public void openLoginPage() {
        openUrl("https://esep.govtec.kz/login");
    }

    public void login(String username, String password, String successUrl) {
        openLoginPage();
        enterText(USERNAME_FIELD, username);
        enterText(PASSWORD_FIELD, password);
        clickElement(LOGIN_BUTTON);

        WebDriverWait localWait = new WebDriverWait(driver, Duration.ofSeconds(10));
        localWait.until(drv -> getCurrentUrl().equals(successUrl));

        String currentUrl = getCurrentUrl();
        Assert.assertEquals(
                currentUrl,
                successUrl,
                "Login failed or wrong redirect. Current URL: " + currentUrl
        );
    }
}
