/**
 * Created by norelltagle on 5/17/16.
 */

import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.*;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;


import java.io.File;
import java.io.IOException;
import java.util.concurrent.TimeUnit;


import static org.junit.Assert.assertEquals;

public class UITestCaseDetails {

    public static final String desktop = "/Users/norelltagle/Desktop/";
    public static final String siteURL = "http://localhost:8000/proto1/#";


    UITestCase test = new UITestCase();

    AutoTesting autotest = new AutoTesting();

    @Test
    public void testUI() throws IOException {

        FirefoxProfile profile = new FirefoxProfile();
        File netExport = new File("/Users/norelltagle/Documents/netExport-0.8.xpi");
        File firebug = new File("/Users/norelltagle/Documents/firebug-2.0.16.xpi");
        profile.addExtension(firebug);
        profile.addExtension(netExport);
        profile.setPreference("app.update.enabled", false);


        String domain = "extensions.firebug.";

// Set default Firebug preferences
        profile.setPreference(domain + "currentVersion", "1.9.2");
        profile.setPreference(domain + "allPagesActivation", "on");
        profile.setPreference(domain + "defaultPanelName", "net");
        profile.setPreference(domain + "net.enableSites", true);

// Set default NetExport preferences
        profile.setPreference(domain + "netexport.alwaysEnableAutoExport", true);
        profile.setPreference(domain + "netexport.showPreview", false);
        profile.setPreference(domain + "netexport.defaultLogDir", desktop);

        WebDriver driver = new FirefoxDriver(profile);

        driver.get(siteURL);

        JavascriptExecutor js = (JavascriptExecutor) driver;
        WebDriverWait wait = new WebDriverWait(driver, 60);

        driver.manage().window().maximize();
        //autotest.loadGooglePage(js, driver);
        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("weblogin_netid")));
       // autotest.loadUWPage(js, driver, wait);
       // autotest.validateOffline(driver, wait);
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
        ExpectedCondition<Boolean> expectation = new
                ExpectedCondition<Boolean>() {
                    public Boolean apply(WebDriver driver) {
                        return ((JavascriptExecutor) driver).executeScript("return document.readyState").equals("complete");
                    }
                };


        String totalCost = autotest.UIvalidation(0, 0, 0, 0, 0, 0, -50, js, wait, driver);
        wait.until(expectation);
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
        wait.until(ExpectedConditions.refreshed(expectation));
        wait.until(expectation);

        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {

        }

        assertEquals("$68,572", totalCost);


    }

}


