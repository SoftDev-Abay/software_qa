package tests;

import com.aventstack.extentreports.ExtentTest;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import pages.LoginPage;
import pages.ReportsRegistryPage;
import utils.DriverFactory;

import java.util.List;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;


public class SearchTests extends BaseTest {

    @DataProvider(name = "searchData")
    public Object[][] searchData() {
        return new Object[][] {
                {
                        "04001",
                        2,
                        new String[][]{
                                {"040010", "Д-9 раздел I. Сведения о специальных организациях образования и численности школ, школ-интернатов, учителей, учащихся"},
                                {"040011", "Д-9 (раздел II). Сведения о распределении учащихся по классам"},
                                {"040012", "Д-9 (раздел III). Сведения о материальной базе специальных организаций образования"},
                                {"040013", "МКШ-1. Сеть и контингент малокомплектных школ (МКШ)"},
                                {"040014", "МКШ-2. Сведения о совмещенных классах и контингенте обучающихся в малокомплектных школах и количество школ по числу учащихся"},
                                {"040015", "МКШ-3. Сведения о малокомплектных школах по языкам обучения, по классам"},
                                {"040016", "МКШ-4. Сведения о материальной базе малокомплектных школ"},
                                {"040017", "МКШ-6. Сведения о качественном составе педагогических кадров малокомплектных школ"},
                                {"040018", "МКШ-10. Сеть ресурсных центров"},
                                {"040019", "СТ-1. Отчет об основных показателях среднего образования"}
                        }
                },
                {
                        "дошкольных",
                        3,
                        new String[][] {
                                {"040001", "ДО-1. Сведения о сети и контингенте детей дошкольных организаций"},
                                {"040002", "ДО-2. Сведения о сети и контингенте детей в дошкольных организациях за исключением мини-центров"},
                                {"040073", "ДО-4. Сведения о дошкольных организациях (группах) по языкам обучения"},
                                {"040075", "ДО-7. Сведения о качественном составе педагогических кадров дошкольных организаций"},
                                {"040076", "ДО-8. Сведения о сети и контингенте дошкольных организаций негосударственной формы собственности"},
                                {"040077", "ДО-9. Сведения о материальной базе дошкольных организаций"},
                                {"040078", "ДО-11. Сведения о специальных дошкольных организациях и о педагогическом составе"},
                                {"040080", "ДО-13. Сведения о сети и контингенте в дошкольных организациях за исключением детских садов"},
                                {"040082", "ДО-15. Сведения о мониторинге открытия и закрытия дошкольных организаций"}
                        }
                }
        };
    }

    @Test(dataProvider = "searchData")
    public void testSearchFunctionality(String searchValue, int columnIndex, String[][] expectedTitles) {
        extentTest = extentReports.createTest("testSearchFunctionality: " + searchValue);

        try {
            LoginPage loginPage = new LoginPage(driver);
            loginPage.login("edugov_admin", "CuShF33o", "https://esep.govtec.kz/admin");
            extentTest.info("Logged in as edugov_admin");

            ReportsRegistryPage registryPage = new ReportsRegistryPage(driver);
            List<List<String>> rowTexts = registryPage.searchInRegistry(searchValue, columnIndex);
            extentTest.info("Search completed for: " + searchValue);

            Thread.sleep(2000);

            for (int i = 0; i < rowTexts.size(); i++) {
                logger.info("Row " + i + " => " + rowTexts.get(i));
            }

            for (String[] expected : expectedTitles) {
                boolean found = false;
                for (List<String> row : rowTexts) {
                    if (row.size() >= 2 && row.get(0).equals(expected[0]) && row.get(1).equals(expected[1])) {
                        found = true;
                        break;
                    }
                }
                Assert.assertTrue(found,
                        "Expected row " + expected[0] + ", " + expected[1] + " not found in results!");
            }

            extentTest.pass("Search test passed with value: " + searchValue);

        } catch (Exception e) {
            extentTest.fail("Search test failed for: " + searchValue + " - " + e.getMessage());
            logger.error("Exception during search test: ", e);
            Assert.fail(e.getMessage());
        }
    }
}
