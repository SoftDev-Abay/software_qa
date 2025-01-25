package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class ReportTemplatePage extends BasePage {

    private final By REPORT_TEMPLATE_TAB = By.xpath("//*[@id='root']/div/div[1]/div[3]/div/div/div[1]/div[2]");
    private final By CREATE_TEMPLATE_BUTTON = By.xpath("//*[@id='root']/div/div[1]/div[3]/div/div/div[2]/div/button");

    private final By TEMPLATE_ID_INPUT       = By.xpath("//*[@id='modal-root']/div/div/div[2]/div[1]/div[2]/input");
    private final By TEMPLATE_NAME_RUS_INPUT = By.xpath("//*[@id='modal-root']/div/div/div[2]/div[2]/div[2]/input");
    private final By TEMPLATE_NAME_KAZ_INPUT = By.xpath("//*[@id='modal-root']/div/div/div[2]/div[3]/div[2]/input");
    private final By TEMPLATE_SUBMIT_BUTTON  = By.xpath("/html/body/div[2]/div/div/div[3]/button[1]");

    public ReportTemplatePage(WebDriver driver) {
        super(driver);
    }


    public void createTemplate(String templateId, String templateNameRus, String templateNameKaz) {
        clickElement(REPORT_TEMPLATE_TAB);
        clickElement(CREATE_TEMPLATE_BUTTON);

        enterText(TEMPLATE_ID_INPUT, templateId);
        enterText(TEMPLATE_NAME_RUS_INPUT, templateNameRus);
        enterText(TEMPLATE_NAME_KAZ_INPUT, templateNameKaz);

        clickElement(TEMPLATE_SUBMIT_BUTTON);

    }
}
