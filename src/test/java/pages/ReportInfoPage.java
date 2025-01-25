package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import utils.DropdownUtils;

public class ReportInfoPage extends BasePage {

    // Example locators matching your Python code
    private final String DROPDOWN_1_XPATH = "/html/body/div[1]/div/div[1]/div[3]/div/div/div[2]/div/div[4]/div[2]/div";
    private final String DROPDOWN_2_XPATH = "//*[@id=\"root\"]/div/div[1]/div[3]/div/div/div[2]/div/div[5]/div[2]/div";
    private final String DROPDOWN_3_XPATH = "//*[@id=\"root\"]/div/div[1]/div[3]/div/div/div[2]/div/div[6]/div[2]/div";

    // Common parent XPath for dropdown options
    private final String PARENT_XPATH = "/html/body/div[3]/div";

    // Input for Template ID
    private final By TEMPLATE_ID_INPUT = By.xpath(
            "//*[@id='root']/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div[2]/input"
    );

    // Submission button after filling info
    private final By SUBMISSION_BUTTON = By.xpath(
            "//*[@id='root']/div/div[1]/div[3]/div/div/div[2]/div/button"
    );

    public ReportInfoPage(WebDriver driver) {
        super(driver);
    }

    /**
     * Open the Report Info page.
     */
    public void openReportInfo(String reportBaseId) {
        String url = "https://esep.govtec.kz/admin/reports/info/" + reportBaseId;
        openUrl(url);
    }

    /**
     * Fill base info with individual dropdown selections and a Template ID.
     */
    public void fillBaseInfo(String templateId) {
        // Select options for each dropdown individually
        DropdownUtils.selectDropdownOption(driver, DROPDOWN_1_XPATH, PARENT_XPATH,
                "Организации государственной и квазигосударственной сфер деятельности");
        DropdownUtils.selectDropdownOption(driver, DROPDOWN_2_XPATH, PARENT_XPATH, "Ежегодно");
        DropdownUtils.selectDropdownOption(driver, DROPDOWN_3_XPATH, PARENT_XPATH, "Да");

        // Fill the template ID input
        enterText(TEMPLATE_ID_INPUT, templateId);

        // Click the submission button
        clickElement(SUBMISSION_BUTTON);
    }
}
