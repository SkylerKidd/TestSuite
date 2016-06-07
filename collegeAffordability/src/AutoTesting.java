/**
 * Created by norelltagle on 4/4/16.
 * <p>
 * //package myPackage;
 * <p>
 * /**
 * Autotesting.java
 * This class contains all the methods that detect and manipulate all the slider bars, table entries and drop down menus
 */


import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.*;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.concurrent.TimeUnit;

import java.util.Properties;

import com.google.gson.*;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

import edu.umass.cs.benchlab.har.tools.HarFileReader;
import org.apache.commons.io.FileUtils;
import org.apache.commons.io.filefilter.WildcardFileFilter;

import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.imageio.ImageIO;
import javax.mail.*;
import javax.mail.internet.*;

//import org.eclipse.jdt.internal.compiler.lookup.SourceTypeBinding;

import org.codehaus.jackson.map.ObjectMapper;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.SystemClock;
import org.openqa.selenium.support.ui.WebDriverWait;

import edu.umass.cs.benchlab.har.*;
import org.w3c.dom.css.Rect;


public class AutoTesting {

    //Paths that would need to be changed eventually
    public static final String desktop = System.getProperty("user.home") + "/Desktop/"; //path for the desktop
    public static final String siteURL = "https://affordability-model.css.uwb.edu/proto1/"; //website URL
    public static final String logFilePrefix = "affordability-model.css.uwb.edu"; //prefix for file name
    public static String netExportPath = "";
    public static String fireBugPath =  "";

    public static final int WAIT_TIME = 60; //wait time for WebDriver
    public String requestLogs = ""; //String where HAR file will be stored

    public static void main(String[] args) throws IOException, Exception {
        //Save these in the
        netExportPath = AutoTesting.class.getProtectionDomain().getCodeSource().getLocation().toURI().getPath().replaceAll("collegeAffordability.jar","").replaceAll("//", "/") + "netExport-0.8.xpi";
        fireBugPath = AutoTesting.class.getProtectionDomain().getCodeSource().getLocation().toURI().getPath().replaceAll("collegeAffordability.jar","").replaceAll("//" , "/") + "firebug-2.0.16.xpi";

        AutoTesting test = new AutoTesting();

        FirefoxProfile profile = new FirefoxProfile();
        File netExport = new File(netExportPath);
        File firebug = new File(fireBugPath);
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

        driver.manage().window().maximize();

        JavascriptExecutor js = (JavascriptExecutor) driver;
        WebDriverWait wait = new WebDriverWait(driver, WAIT_TIME); //Have a maximum wait of 60 seconds

        wait.until(ExpectedConditions.presenceOfElementLocated(By.id("weblogin_netid")));

        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));


       String toExecute = "$('#calendar_year').val('2017').change();";
        js.executeScript(toExecute);

        System.out.println("Done!");
      //  test.testallTables(wait, driver, js);
     //   test.testAllDropDowns(wait, driver, js);
      //  test.testAllSliders(wait,driver,js);
        Thread.sleep(5000);
        test.scanAndSendHAR(driver);
        //test.takeScreenshot2(driver);
        // test.UIvalidation(driver, js, wait);
        System.out.println("Done for real!");

    }



    //testAllTables
    //Finds all table entries, filters out the ones that can be changed by the user, grabs their min and max values
    //and iterates through each step
    public void testallTables(WebDriverWait wait, WebDriver driver, JavascriptExecutor js) throws StaleElementReferenceException {
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
        List<WebElement> allTableEntries = driver.findElements(By.tagName("td"));
        for (WebElement tableEntry : allTableEntries) {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));

            //NOTE:
            //This try catch block was a quick, temporary fix. Find a better way to handle StaleElementReferenceException, if possible
            try {
                wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("input")));
                List<WebElement> inputEntries = tableEntry.findElements(By.tagName("input"));
                for (WebElement entry : inputEntries) {
                    wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
                    if (entry.getAttribute("disabled") == null) {
                        String type = entry.getAttribute("type");
                        if (type.equals("number")) {
                            String id = entry.getAttribute("id");
                            String dataScenario = entry.getAttribute("data-scenario");
                            double min = Double.parseDouble(entry.getAttribute("min"));
                            double max = Double.parseDouble(entry.getAttribute("max"));
                            String step = entry.getAttribute("step");
                            double interval = 0;
                            if (step == null || step.isEmpty()) {
                                interval = 10;
                            } else {
                                interval = Double.parseDouble(step);
                            }

                            for (double i = min; i <= max; i += interval) {
                                wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
                                String toExecute = "$('[data-scenario=\"" + dataScenario + "\"]').val('" + i + "').change();";
                                js.executeScript(toExecute);
                            }
                        }
                    }
                }
            } catch (StaleElementReferenceException e) {
                return;
            }

        }

    }

    //testAllDropDowns
    //Finds all drop downs and iterates through all of its options
    //Assumption: All drop downs have the tag name "select"
    public void testAllDropDowns(WebDriverWait wait, WebDriver driver, JavascriptExecutor js) {
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
        List<WebElement> allDropDowns = driver.findElements(By.tagName("select"));
        for (WebElement element : allDropDowns) {
            String id = element.getAttribute("id");
            List<WebElement> options = element.findElements(By.tagName("option"));
            for (WebElement option : options) {
                wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
                String toExecute = "$('#" + id + "').val('" + option.getAttribute("value") + "').change();";
                js.executeScript(toExecute);

            }
        }

    }

    //testAllSliders
    //Finds all sliders and iterates through slider bar and text box value
    //Assumption: All sliders are under the class name "input-group"
    public void testAllSliders(WebDriverWait wait, WebDriver driver, JavascriptExecutor js) {
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
        List<WebElement> allSliders = driver.findElements(By.className("input-group"));
        for (WebElement element : allSliders) {
            String dataFor = element.findElement(By.tagName("div")).getAttribute("data-for");
            int max = Integer.parseInt(element.findElement(By.tagName("input")).getAttribute("max"));
            for (int i = 0; i <= max; i += 10) {
                wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
                double normalize = ((double) i / max) * 100.0;
                String textBoxID = element.findElement(By.tagName("input")).getAttribute("id");
                //get text box
                //jquery to change text box
                String toExecute = "$('#" + textBoxID + "').val('" + i + "').change();";
                //jquery to change left
                toExecute += "$('div[data-for=\"" + dataFor + "\"]').find('span').attr('style', 'left: " + normalize + "%');";
                System.out.println(toExecute);
                js.executeScript(toExecute);

            }
        }

    }

    //scanAndSendHar
    //Records all the requests and responses throughu
    public void scanAndSendHAR(WebDriver driver) throws IOException, AWTException {

        File dir = new File(desktop);
        //String requestLogs = "";
        FileFilter filter = new WildcardFileFilter(logFilePrefix + "*.har");
        FileFilter otherFiles = new WildcardFileFilter("*.har");
        for (File file : dir.listFiles()) {
            if (filter.accept(file)) {
                System.out.println("file accepted");
                HarFileReader r = new HarFileReader();
                HarLog log = r.readHarFile(file);

                HarEntries entries = log.getEntries();
                for (HarEntry entry : entries.getEntries()) {
                    if (entry.getResponse().getStatus() == 500) {
                        requestLogs += "RESPONSE\n";
                        requestLogs += "response:\n" + entry.getResponse().getStatus() + "\n";
                        requestLogs += "status: " + entry.getResponse().getStatusText() + "\n\n";
                        requestLogs += "REQUEST\n";
                        // requestLogs += entry.getRequest().getPostData().toString()+ "\n\n";

                        String allParams = "{" + entry.getRequest().getPostData().getParams().toString() + "}";

                        //Fix the string because the library doesn't actually format it into proper JSON
                        allParams = allParams.replaceAll(",  }", "}").replaceAll("\"\\[", "[").replaceAll("\\]\"", "]").replaceAll("\"\\{", "{").replaceAll("}\"", "}").replaceAll(":null", ":\"null\"");

                        //Format the file into proper JSON
                        JsonParser parser = new JsonParser();
                        Gson gson = new GsonBuilder().setPrettyPrinting().create();

                        JsonElement el = parser.parse(allParams);
                        allParams = gson.toJson(el); // done

                        requestLogs += allParams + "\n\n";

                       System.out.println("writing to log");
                    }
                }
                file.delete();
            } else if (otherFiles.accept(file)) {
                file.delete();
            }
        }
        if (!requestLogs.isEmpty()) {
            // sendEmail(requestLogs);
            String timeStamp = new SimpleDateFormat("MM.dd.yyyy.HH.mm.ss").format(new Date());
            File har = new File(desktop + "HARlog-" + timeStamp);
            har.mkdir();

            PrintWriter out = new PrintWriter(har.getAbsolutePath() + "/HARfile.txt");
            out.println(requestLogs);


            out.close();
            takeScreenshot2(driver, har.getAbsolutePath() + "/screenshot.png");


        }
    }

    //takeScreenshot
    //Takes screenshot of window of driver
    public void takeScreenshot2(WebDriver driver, String filePath) {
        File screenshot = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE);

        try {
            FileUtils.copyFile(screenshot, new File(filePath));
            System.out.println("Screenshot taken!");

        } catch (IOException e) {
            e.printStackTrace();

        }
    }

    public void takeScreenshot() throws AWTException, IOException {

        Graphics2D imageGraphics = null;
        Robot robot = new Robot();
        GraphicsDevice currentDevice = MouseInfo.getPointerInfo()
                .getDevice();
        BufferedImage exportImage = robot.createScreenCapture(currentDevice
                .getDefaultConfiguration().getBounds());

        imageGraphics = (Graphics2D) exportImage.getGraphics();
        ImageIO.write(exportImage, "png", new File(desktop + "screenshot.jpg")); //this is going to need to change


    }


    public void sendEmail(String requestLogs) throws FileNotFoundException, IOException, AWTException {
        takeScreenshot();
        String username = "collegeaffordabilitytests@gmail.com";
        String password = "uwbothell";

        Properties props = new Properties();
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.host", "smtp.gmail.com");
        props.put("mail.smtp.port", "587");

        Session session = Session.getInstance(props, new javax.mail.Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });

        try {
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress("norelltagle@gmail.com"));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse("norelltagle@gmail.com"));
            message.setSubject("Test Results");
            BodyPart messageBodyPart = new MimeBodyPart();

            // Now set the actual message
            messageBodyPart.setText("Here are the results of the test\n");

            // Create a multipar message
            Multipart multipart = new MimeMultipart();

            // Set text message part
            multipart.addBodyPart(messageBodyPart);

            // Part two is attachment
            messageBodyPart = new MimeBodyPart();
            String filename = "HARfile.txt";
            File file = new File(filename);

            PrintWriter fileWriter = new PrintWriter(filename);
            fileWriter.write(requestLogs);
            fileWriter.close();

            DataSource source = new FileDataSource(filename);
            messageBodyPart.setDataHandler(new DataHandler(source));
            messageBodyPart.setFileName(filename);
            multipart.addBodyPart(messageBodyPart);

            messageBodyPart = new MimeBodyPart();
            String screenshotPath = desktop + "screenshot.jpg";
            source = new FileDataSource(screenshotPath);
            messageBodyPart.setDataHandler(new DataHandler(source));
            messageBodyPart.setFileName(screenshotPath);
            multipart.addBodyPart(messageBodyPart);

            message.setContent(multipart);

            Transport.send(message);
            file.delete();
            System.out.println("email sent!");
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }
    }


    @Test
    //Use nominal sets as arguments
    public String UIvalidation(String year, int family_income_exclusion, int family_income_contribution, int percent_disc_income_saved, int years_of_saving, int interest_on_savings, int hours_worked, int tuition_adjustment, JavascriptExecutor js, WebDriverWait wait, WebDriver driver) {

        String toReturn = "";

        String toExecute = "$('#calendar_year').val('" + year + "').change();";
        toExecute += "$('#family_income_exclusion_threshold').val('" + family_income_exclusion + "').change();";
        toExecute += "$('#discretionary_income_contribution').val('" + family_income_contribution + "').change();";
        toExecute += "$('#percent_discretionary_income_saved').val('" + percent_disc_income_saved + "').change();";
        toExecute += "$('#years_of_savings').val('" + years_of_saving + "').change();";
        toExecute += "$('#interest_earned').val('" + interest_on_savings + "').change();";
        toExecute += "$('#hours_worked').val('" + hours_worked + "').change();";
        toExecute += "$('#policy_change_tuition_adjustment').val('" + tuition_adjustment + "').change();";
        js.executeScript(toExecute);

        wait.until(ExpectedConditions.attributeContains(By.id("policy_change_tuition_adjustment"), "value", Integer.toString(tuition_adjustment)));

        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));

        ExpectedCondition<Boolean> expectation = new
                ExpectedCondition<Boolean>() {
                    public Boolean apply(WebDriver driver) {
                        return ((JavascriptExecutor) driver).executeScript("return document.readyState").equals("complete");
                    }
                };

        wait.until(expectation);
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
        wait.until(ExpectedConditions.refreshed(expectation));
        wait.until(expectation);

        String totalCost = driver.findElement(By.id("ui_total_coa")).getText();

        return totalCost;

    }


    public void UIvalidation(WebDriver driver, JavascriptExecutor js, WebDriverWait wait) {
        UITestCase[] cases = new UITestCase[]{
                new UITestCase(0, 0, 0, 0, 0, 0, -50, "$68,572"),
                new UITestCase(400, 40, 40, 20, 10, 1000, 50, "$99,716"),
                new UITestCase(200, 10, 5, 10, 1, 500, 0, "$84,144")

        };

        for (UITestCase theCase : cases) {
            {
                String toExecute = "$('#family_income_exclusion_threshold').val('" + theCase.getFamily_income_exclusion() + "').change();";
                toExecute += "$('#discretionary_income_contribution').val('" + theCase.getFamily_income_contribution() + "').change();";
                toExecute += "$('#percent_discretionary_income_saved').val('" + theCase.getPercent_disc_income_saved() + "').change();";
                toExecute += "$('#years_of_savings').val('" + theCase.getYears_of_saving() + "').change();";
                toExecute += "$('#interest_earned').val('" + theCase.getInterest_on_savings() + "').change();";
                toExecute += "$('#hours_worked').val('" + theCase.getHours_worked() + "').change();";
                toExecute += "$('#policy_change_tuition_adjustment').val('" + theCase.getTuition_adjustment() + "').change();";
                js.executeScript(toExecute);
                System.out.println(toExecute);

                wait.until(ExpectedConditions.attributeContains(By.id("policy_change_tuition_adjustment"), "value", Integer.toString(theCase.getTuition_adjustment())));

                wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("ui_total_coa")));
                String totalCost = driver.findElement(By.id("ui_total_coa")).getText();

                System.out.println(totalCost);

                assertEquals(theCase.getTotalCost(), totalCost);

                if (totalCost.equals(theCase.getTotalCost())) {

                    System.out.println("UI MATCH!");
                    requestLogs += "UI ERROR!\n";

                }

            }
        }

    }


}
