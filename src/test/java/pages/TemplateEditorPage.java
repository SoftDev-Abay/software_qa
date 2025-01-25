package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;

public class TemplateEditorPage extends BasePage {

    private final By CREATE_TABLE_BUTTON  = By.xpath("//*[@id=\"root\"]/div/div[1]/div[3]/div/div/div/div/div/div/button[1]");
    private final By SAVE_TEMPLATE_BUTTON = By.xpath("//*[@id=\"root\"]/div/div[1]/div[3]/div/div/div/div/div/div[1]/button[2]");

    private final By TABLE_NAME_INPUT = By.cssSelector("body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div:nth-child(1) > div > input[type='text']");
    private final By STATIC_BUTTON    = By.cssSelector("body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-i9qltj > div:nth-child(1) > div");
    private final By DYNAMIC_BUTTON   = By.cssSelector("body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.MuiGrid-root.MuiGrid-container.MuiGrid-spacing-xs-2.css-i9qltj > div:nth-child(2) > div");
    private final By ROW_COUNT_INPUT  = By.cssSelector("body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.body-footer > div:nth-child(1) > div > input[type=number]");
    private final By COL_COUNT_INPUT  = By.cssSelector("body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-body > div.body-footer > div:nth-child(2) > div > input[type=number]");
    private final By SUBMIT_TABLE_BTN = By.cssSelector("body > div.MuiModal-root.css-8ndowl > div.MuiBox-root.css-vtxhf1 > div.modal-footer > button:nth-child(2)");

    public TemplateEditorPage(WebDriver driver) {
        super(driver);
    }

    public void openTemplateEditor(String templateId) {
        String url = "https://esep.govtec.kz/admin/reports/templateEditor/" + templateId;
        openUrl(url);
    }

    public void createTable(String tableName, boolean isStatic, int rowCount, int colCount) {
        clickElement(CREATE_TABLE_BUTTON);
        enterText(TABLE_NAME_INPUT, tableName);

        if (isStatic) {
            clickElement(STATIC_BUTTON);
        } else {
            clickElement(DYNAMIC_BUTTON);
        }

        enterText(ROW_COUNT_INPUT, String.valueOf(rowCount));
        enterText(COL_COUNT_INPUT, String.valueOf(colCount));

        clickElement(SUBMIT_TABLE_BTN);
    }

    public void saveTemplate() {
        clickElement(SAVE_TEMPLATE_BUTTON);
    }
}
