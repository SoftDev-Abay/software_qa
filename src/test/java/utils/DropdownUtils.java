package utils;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.List;

public class DropdownUtils {

    public static boolean selectDropdownOption(WebDriver driver, String selectXpath, String parentXpath, String optionText) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

            WebElement dropdown = wait.until(ExpectedConditions.elementToBeClickable(By.xpath(selectXpath)));
            ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", dropdown);
            dropdown.click();
            System.out.println("Dropdown at '" + selectXpath + "' clicked.");

            WebElement dropdownContainer = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(parentXpath)));
            System.out.println("Dropdown container found at '" + parentXpath + "'.");

            wait.until(ExpectedConditions.visibilityOf(dropdownContainer));

            List<WebElement> options = dropdownContainer.findElements(By.xpath(".//div"));
            System.out.println("Found " + options.size() + " options in the dropdown.");

            System.out.println("Options found: '" + options + "'");



            for (WebElement option : options) {
                String text = option.getText().trim();
                System.out.println("Option found: '" + text + "'");
                if (text.equals(optionText)) {
                    option.click();
                    System.out.println("Option '" + optionText + "' selected successfully.");
                    return true;
                }
            }

            System.out.println("Option '" + optionText + "' not found in the dropdown!");
            return false;

        } catch (TimeoutException e) {
            System.out.println("Timeout while handling dropdown at '" + selectXpath + "': " + e.getMessage());
            return false;
        } catch (Exception e) {
            System.out.println("An error occurred while selecting the dropdown option: " + e.getMessage());
            return false;
        }
    }

    public static void fillInputWithValue(WebDriver driver, String inputXpath, String value) {
        try {
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
            WebElement inputElem = wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(inputXpath)));
            inputElem.clear();
            inputElem.sendKeys(value);
        } catch (Exception e) {
            System.out.println("An error occurred while filling input: " + e.getMessage());
        }
    }
}
