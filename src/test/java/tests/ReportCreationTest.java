package tests;

import com.aventstack.extentreports.ExtentTest;
import org.testng.Assert;
import org.testng.annotations.Test;
import pages.LoginPage;
import pages.ReportsRegistryPage;
import pages.ReportInfoPage;
import pages.ReportTemplatePage;
import pages.TemplateEditorPage;

public class ReportCreationTest extends BaseTest {

    @Test
    public void testCreateFullReportFlow() {
        extentTest = extentReports.createTest("testCreateFullReportFlow");
         logger.info("Starting test to create a full report with base + info + template + table.");

        try {
            // 1) LOGIN as admin
            LoginPage loginPage = new LoginPage(driver);
            loginPage.login("edugov_admin", "CuShF33o", "https://esep.govtec.kz/admin");
            extentTest.info("Logged in as edugov_admin.");

            // 2) GO to Reports Registry + Create Report Base
            ReportsRegistryPage registryPage = new ReportsRegistryPage(driver);
            registryPage.openReportsRegistry();
            String reportBaseId = "testing_qa19";
            String reportBaseNameRus = "Тестовый отчет";
            String reportBaseNameKaz = "Сынақ есеп";
            registryPage.createReportBase(reportBaseId, reportBaseNameRus, reportBaseNameKaz);
            extentTest.info("Created new report base ID: " + reportBaseId);

            // 3) FILL Additional Info on the “Report Info” page
            ReportInfoPage reportInfoPage = new ReportInfoPage(driver);
            reportInfoPage.openReportInfo(reportBaseId);

            String templateId = "testing_qa19";
            reportInfoPage.fillBaseInfo(templateId);
            extentTest.info("Filled additional base info with templateId: " + templateId);

            // 4) CREATE a New Template
            ReportTemplatePage reportTemplatePage = new ReportTemplatePage(driver);
            String templateNameRus = "Шаблон отчета";
            String templateNameKaz = "Есеп үлгісі";
            reportTemplatePage.createTemplate(templateId, templateNameRus, templateNameKaz);
            extentTest.info("Created new report template: " + templateId);

            // 5) OPEN Template Editor and CREATE Table
            TemplateEditorPage templateEditor = new TemplateEditorPage(driver);
            templateEditor.openTemplateEditor(templateId);

            String tableName = "Table1";
            templateEditor.createTable(tableName, true, 5, 4);
            extentTest.info("Created table: " + tableName);

            // 6) SAVE Template
            templateEditor.saveTemplate();
            extentTest.pass("Template saved successfully.");

        } catch (Exception e) {
            extentTest.fail("Exception during testCreateFullReportFlow: " + e.getMessage());
             logger.error("Error in testCreateFullReportFlow", e);
            Assert.fail(e.getMessage());
        }
    }
}
