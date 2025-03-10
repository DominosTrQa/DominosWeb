package WebAutomationBase.step;

import WebAutomationBase.base.BaseTest;
import WebAutomationBase.helper.ElementHelper;
import WebAutomationBase.helper.StoreHelper;
import WebAutomationBase.model.ElementInfo;
import com.thoughtworks.gauge.Step;

import java.io.Console;
import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

import org.apache.log4j.PropertyConfigurator;
import org.junit.Assert;
import org.junit.Test;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import org.slf4j.LoggerFactory;
import org.slf4j.impl.Log4jLoggerAdapter;

import static org.openqa.selenium.Keys.BACK_SPACE;

public class BaseSteps extends BaseTest {


  public static int DEFAULT_MAX_ITERATION_COUNT = 150;
  public static int DEFAULT_MILLISECOND_WAIT_AMOUNT = 100;

  private static Log4jLoggerAdapter logger = (Log4jLoggerAdapter) LoggerFactory
          .getLogger(BaseSteps.class);

  private static String SAVED_ATTRIBUTE;

  private Actions actions = new Actions(driver);
  private BaseSteps webDriver;

  public BaseSteps(){

    PropertyConfigurator
            .configure(BaseSteps.class.getClassLoader().getResource("log4j.properties"));
  }

  private WebElement findElement(String key){
    ElementInfo elementInfo = StoreHelper.INSTANCE.findElementInfoByKey(key);
    By infoParam = ElementHelper.getElementInfoToBy(elementInfo);
    WebDriverWait webDriverWait = new WebDriverWait(driver, 0);
    WebElement webElement = webDriverWait
            .until(ExpectedConditions.presenceOfElementLocated(infoParam));
    ((JavascriptExecutor) driver).executeScript(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})",
            webElement);
    return webElement;
  }

  private List<WebElement> findElements(String key){
    ElementInfo elementInfo = StoreHelper.INSTANCE.findElementInfoByKey(key);
    By infoParam = ElementHelper.getElementInfoToBy(elementInfo);
    return driver.findElements(infoParam);
  }

  private void clickElement(WebElement element){
    element.click();
  }

  private void clickElementBy(String key){
    findElement(key).click();
  }

  private void hoverElement(WebElement element){
    actions.moveToElement(element).build().perform();
  }

  private void hoverElementBy(String key){
    WebElement webElement = findElement(key);
    actions.moveToElement(webElement).build().perform();
  }

  private void sendKeyESC(String key){
    findElement(key).sendKeys(Keys.ESCAPE);

  }

  private boolean isDisplayed(WebElement element){
    return element.isDisplayed();
  }

  private boolean isDisplayedBy(By by){
    return driver.findElement(by).isDisplayed();
  }

  private String getPageSource(){
    return driver.switchTo().alert().getText();
  }

  public static String getSavedAttribute(){
    return SAVED_ATTRIBUTE;
  }

  public String randomString(int stringLength){

    Random random = new Random();
    char[] chars = "ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz0123456789".toCharArray();
    String stringRandom = "";
    for (int i = 0; i < stringLength; i++) {

      stringRandom = stringRandom + String.valueOf(chars[random.nextInt(chars.length)]);
    }

    return stringRandom;
  }

  public WebElement findElementWithKey(String key){
    return findElement(key);
  }

  public String getElementText(String key){
    return findElement(key).getText();
  }

  public String getElementAttributeValue(String key, String attribute){
    return findElement(key).getAttribute(attribute);
  }

  @Step("Print page source")
  public void printPageSource(){
    System.out.println(getPageSource());
  }

  public void javaScriptClicker(WebDriver driver, WebElement element){

    JavascriptExecutor jse = ((JavascriptExecutor) driver);
    jse.executeScript("var evt = document.createEvent('MouseEvents');"
            + "evt.initMouseEvent('click',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);"
            + "arguments[0].dispatchEvent(evt);", element);
  }

  @Step({"Wait <value> seconds",
          "<int> saniye bekle"})
  public void waitBySeconds(int seconds){
    try {
      logger.info(seconds + " saniye bekleniyor.");
      Thread.sleep(seconds * 1000);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }

  @Step({"Wait <value> milliseconds",
          "<long> milisaniye bekle"})
  public void waitByMilliSeconds(long milliseconds){
    try {
      logger.info(milliseconds + " milisaniye bekleniyor.");
      Thread.sleep(milliseconds);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }

  @Step({"Wait for element then click <key>",
          "Elementi bekle ve sonra tıkla <key>"})
  public void checkElementExistsThenClick(String key){
    getElementWithKeyIfExists(key);
    clickElement(key);
  }

  @Step({"Wait for element then click <key> try",
          "Elementi bekle ve sonra tıkla <key> try"})
  public void checkElementExistsThenClickTryCatch(String key){
    try {
      clickElement(key);
    } catch (Exception e){
      logger.info("Tek test şubesi var");
    }

  }

  @Step({"Elementini bekle ve hemen tıkla <key>"})
  public void hemenTikla(String key){
    WebElement webElement;
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      try {
        webElement = findElementWithKey(key);
        clickElement(webElement);
        logger.info(key + " elementine tıklandı.");
        return;
      } catch (WebDriverException e) {
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element: '" + key + "' doesn't exist.");
    return;
  }

  @Step({"Click to element <key>",
          "Elementine tıkla <key>"})
  public void clickElement(String key){
    if (!key.equals("")) {
      WebElement element = findElement(key);
      hoverElement(element);
      waitByMilliSeconds(500);
      clickElement(element);
      logger.info(key + " elementine tıklandı.");
    }
  }

  @Step({"Click to element <key> with focus",
          "<key> elementine focus ile tıkla"})
  public void clickElementWithFocus(String key){
    actions.moveToElement(findElement(key));
    actions.click();
    actions.build().perform();
    logger.info(key + " elementine focus ile tıklandı.");
  }

  @Step({"Check if element <key> exists",
          "Wait for element to load with key <key>",
          "Element var mı kontrol et <key>",
          "Elementin yüklenmesini bekle <key>"})
  public WebElement getElementWithKeyIfExists(String key){
    WebElement webElement;
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      try {
        webElement = findElementWithKey(key);
        logger.info(key + " elementi bulundu.");
        return webElement;
      } catch (WebDriverException e) {
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element: '" + key + "' doesn't exist.");
    return null;
  }


  @Step({"Go to <url> address",
          "<url> adresine git"})
  public void goToUrl(String url){
    driver.get(url);
    logger.info(url + " adresine gidiliyor.");
  }

  @Step({"Wait for element to load with css <css>",
          "Elementin yüklenmesini bekle css <css>"})
  public void waitElementLoadWithCss(String css){
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      if (driver.findElements(By.cssSelector(css)).size() > 0) {
        logger.info(css + " elementi bulundu.");
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element: '" + css + "' doesn't exist.");
  }

  @Step({"Wait for element to load with xpath <xpath>",
          "Elementinin yüklenmesini bekle xpath <xpath>"})
  public void waitElementLoadWithXpath(String xpath){
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      if (driver.findElements(By.xpath(xpath)).size() > 0) {
        logger.info(xpath + " elementi bulundu.");
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element: '" + xpath + "' doesn't exist.");
  }

  @Step({"Check if element <key> exists else print message <message>",
          "Element <key> var mı kontrol et yoksa hata mesajı ver <message>"})
  public void getElementWithKeyIfExistsWithMessage(String key, String message){
    ElementInfo elementInfo = StoreHelper.INSTANCE.findElementInfoByKey(key);
    By by = ElementHelper.getElementInfoToBy(elementInfo);

    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      if (driver.findElements(by).size() > 0) {
        logger.info(key + " elementi bulundu.");
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail(message);
  }

  @Step({"Check if element <key> not exists",
          "Element yok mu kontrol et <key>"})
  public void checkElementNotExists(String key){
    ElementInfo elementInfo = StoreHelper.INSTANCE.findElementInfoByKey(key);
    By by = ElementHelper.getElementInfoToBy(elementInfo);

    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      if (driver.findElements(by).size() == 0) {
        logger.info(key + " elementinin olmadığı kontrol edildi.");
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element '" + key + "' still exist.");
  }

  @Step({"Upload file in project <path> to element <key>",
          "Proje içindeki <path> dosyayı <key> elemente upload et"})
  public void uploadFile(String path, String key){
    String pathString = System.getProperty("user.dir") + "/";
    pathString = pathString + path;
    findElement(key).sendKeys(pathString);
    logger.info(path + " dosyası " + key + " elementine yüklendi.");
  }

  @Step({"Write value <text> to element <key>",
          "<text> textini <key> elemente yaz"})
  public void sendKeys(String text, String key){
    if (!key.equals("")) {
      findElement(key).sendKeys(text);
      logger.info(key + " elementine " + text + " texti yazıldı.");
    }
  }

  @Step({"Click with javascript to css <css>",
          "Javascript ile css tıkla <css>"})
  public void javascriptClickerWithCss(String css){
    Assert.assertTrue("Element bulunamadı", isDisplayedBy(By.cssSelector(css)));
    javaScriptClicker(driver, driver.findElement(By.cssSelector(css)));
    logger.info("Javascript ile " + css + " tıklandı.");
  }

  @Step({"Click with javascript to xpath <xpath>",
          "Javascript ile xpath tıkla <xpath>"})
  public void javascriptClickerWithXpath(String xpath){
    Assert.assertTrue("Element bulunamadı", isDisplayedBy(By.xpath(xpath)));
    javaScriptClicker(driver, driver.findElement(By.xpath(xpath)));
    logger.info("Javascript ile " + xpath + " tıklandı.");
  }

  @Step({"Check if current URL contains the value <expectedURL>",
          "Şuanki URL <url> değerini içeriyor mu kontrol et"})
  public void checkURLContainsRepeat(String expectedURL){
    int loopCount = 0;
    String actualURL = "";
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      actualURL = driver.getCurrentUrl();

      if (actualURL != null && actualURL.contains(expectedURL)) {
        logger.info("Şuanki URL" + expectedURL + " değerini içeriyor.");
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail(
            "Actual URL doesn't match the expected." + "Expected: " + expectedURL + ", Actual: "
                    + actualURL);
  }

  @Step({"Send TAB key to element <key>",
          "Elemente TAB keyi yolla <key>"})
  public void sendKeyToElementTAB(String key){
    findElement(key).sendKeys(Keys.TAB);
    logger.info(key + " elementine TAB keyi yollandı.");
  }

  @Step({"Send BACKSPACE key to element <key>",
          "Elemente BACKSPACE keyi yolla <key>"})
  public void sendKeyToElementBACKSPACE(String key){
    findElement(key).sendKeys(BACK_SPACE);
    logger.info(key + " elementine BACKSPACE keyi yollandı.");
  }

  @Step({"Send ESCAPE key to element <key>",
          "Elemente ESCAPE keyi yolla <key>"})
  public void sendKeyToElementESCAPE(String key){
    findElement(key).sendKeys(Keys.ESCAPE);
    logger.info(key + " elementine ESCAPE keyi yollandı.");
  }

  @Step({"Check if element <key> has attribute <attribute>",
          "<key> elementi <attribute> niteliğine sahip mi"})
  public void checkElementAttributeExists(String key, String attribute){
    WebElement element = findElement(key);
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      if (element.getAttribute(attribute) != null) {
        logger.info(key + " elementi " + attribute + " niteliğine sahip.");
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element DOESN't have the attribute: '" + attribute + "'");
  }

  @Step({"Check if element <key> not have attribute <attribute>",
          "<key> elementi <attribute> niteliğine sahip değil mi"})
  public void checkElementAttributeNotExists(String key, String attribute){
    WebElement element = findElement(key);

    int loopCount = 0;

    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      if (element.getAttribute(attribute) == null) {
        logger.info(key + " elementi " + attribute + " niteliğine sahip olmadığı kontrol edildi.");
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element STILL have the attribute: '" + attribute + "'");
  }

  @Step({"Check if <key> element's attribute <attribute> equals to the value <expectedValue>",
          "<key> elementinin <attribute> niteliği <value> değerine sahip mi"})
  public void checkElementAttributeEquals(String key, String attribute, String expectedValue){
    WebElement element = findElement(key);

    String actualValue;
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      actualValue = element.getAttribute(attribute).trim();
      if (actualValue.equals(expectedValue)) {
        logger.info(
                key + " elementinin " + attribute + " niteliği " + expectedValue + " değerine sahip.");
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element's attribute value doesn't match expected value");
  }

  @Step({"Check if <key> element's attribute <attribute> contains the value <expectedValue>",
          "<key> elementinin <attribute> niteliği <value> değerini içeriyor mu"})
  public void checkElementAttributeContains(String key, String attribute, String expectedValue){
    WebElement element = findElement(key);

    String actualValue;
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      actualValue = element.getAttribute(attribute).trim();
      if (actualValue.contains(expectedValue)) {
        return;
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element's attribute value doesn't contain expected value");
  }

  @Step({"Write <value> to <attributeName> of element <key>",
          "<value> değerini <attribute> niteliğine <key> elementi için yaz"})
  public void setElementAttribute(String value, String attributeName, String key){
    String attributeValue = findElement(key).getAttribute(attributeName);
    findElement(key).sendKeys(attributeValue, value);
  }

  @Step({"Write <value> to <attributeName> of element <key> with Js",
          "<value> değerini <attribute> niteliğine <key> elementi için JS ile yaz"})
  public void setElementAttributeWithJs(String value, String attributeName, String key){
    WebElement webElement = findElement(key);
    JavascriptExecutor js = (JavascriptExecutor) driver;
    js.executeScript("arguments[0].setAttribute('" + attributeName + "', '" + value + "')",
            webElement);
  }

  @Step({"Clear text of element <key>",
          "<key> elementinin text alanını temizle"})
  public void clearInputArea(String key){
    findElement(key).clear();
  }

  @Step({"Clear text of element <key> with BACKSPACE",
          "<key> elementinin text alanını BACKSPACE ile temizle"})
  public void clearInputAreaWithBackspace(String key){
    WebElement element = findElement(key);
    element.clear();
    element.sendKeys("a");
    actions.sendKeys(BACK_SPACE).build().perform();
  }

  @Step({"Save attribute <attribute> value of element <key>",
          "<attribute> niteliğini sakla <key> elementi için"})
  public void saveAttributeValueOfElement(String attribute, String key){
    SAVED_ATTRIBUTE = findElement(key).getAttribute(attribute);
    System.out.println("Saved attribute value is: " + SAVED_ATTRIBUTE);
  }

  @Step({"Write saved attribute value to element <key>",
          "Kaydedilmiş niteliği <key> elementine yaz"})
  public void writeSavedAttributeToElement(String key){
    findElement(key).sendKeys(SAVED_ATTRIBUTE);
  }

  @Step({"Check if element <key> contains text <expectedText>",
          "<key> elementi <text> değerini içeriyor mu kontrol et"})
  public void checkElementContainsText(String key, String expectedText){
    Boolean containsText = findElement(key).getText().contains(expectedText);
    Assert.assertTrue("Expected text is not contained", containsText);
  }

  @Step({"Write random value to element <key>",
          "<key> elementine random değer yaz"})
  public void writeRandomValueToElement(String key){
    findElement(key).sendKeys(randomString(15));
  }

  @Step({"Write random value to element <key> starting with <text>",
          "<key> elementine <text> değeri ile başlayan random değer yaz"})
  public void writeRandomValueToElement(String key, String startingText){
    String randomText = startingText + randomString(15);
    findElement(key).sendKeys(randomText);
  }

  @Step({"Print element text by css <css>",
          "Elementin text değerini yazdır css <css>"})
  public void printElementText(String css){
    System.out.println(driver.findElement(By.cssSelector(css)).getText());
  }

  @Step({"Write value <string> to element <key> with focus",
          "<string> değerini <key> elementine focus ile yaz"})
  public void sendKeysWithFocus(String text, String key){
    actions.moveToElement(findElement(key));
    actions.click();
    actions.sendKeys(text);
    actions.build().perform();
  }

  @Step({"Refresh page",
          "Sayfayı yenile"})
  public void refreshPage(){
    driver.navigate().refresh();
  }

  @Step({"Change page zoom to <value>%",
          "Sayfanın zoom değerini değiştir <value>%"})
  public void chromeZoomOut(String value){
    JavascriptExecutor jsExec = (JavascriptExecutor) driver;
    jsExec.executeScript("document.body.style.zoom = '" + value + "%'");
  }

  @Step({"Open new tab",
          "Yeni sekme aç"})
  public void chromeOpenNewTab(){
    ((JavascriptExecutor) driver).executeScript("window.open()");
  }

  @Step({"Focus on tab number <number>",
          "<number> numaralı sekmeye odaklan"})//Starting from 1
  public void chromeFocusTabWithNumber(int number){
    ArrayList<String> tabs = new ArrayList<>(driver.getWindowHandles());
    driver.switchTo().window(tabs.get(number - 1));
  }

  @Step({"Focus on last tab",
          "Son sekmeye odaklan"})
  public void chromeFocusLastTab(){
    ArrayList<String> tabs = new ArrayList<>(driver.getWindowHandles());
    driver.switchTo().window(tabs.get(tabs.size() - 1));
  }

  @Step({"Focus on frame with <key>",
          "Frame'e odaklan <key>"})
  public void chromeFocusFrameWithNumber(String key){
    WebElement webElement = findElement(key);
    driver.switchTo().frame(webElement);
  }

  @Step({"Accept Chrome alert popup",
          "Chrome uyarı popup'ını kabul et"})
  public void acceptChromeAlertPopup(){
    driver.switchTo().alert().accept();
  }


  //----------------------SONRADAN YAZILANLAR-----------------------------------

  private JavascriptExecutor getJSExecutor() {
    return (JavascriptExecutor) driver;
  }
  private Object executeJS(String script, boolean wait) {
    return wait ? getJSExecutor().executeScript(script, "") : getJSExecutor().executeAsyncScript(script, "");
  }
  private void scrollTo(int x, int y) {
    String script = String.format("window.scrollTo(%d, %d);", x, y);
    executeJS(script, true);
  }
  public WebElement scrollToElementToBeVisible(String key) {
    ElementInfo elementInfo = StoreHelper.INSTANCE.findElementInfoByKey(key);
    WebElement webElement =driver.findElement(ElementHelper.getElementInfoToBy(elementInfo));
    if (webElement != null) {
      scrollTo(webElement.getLocation().getX(), webElement.getLocation().getY() - 100);
    }
    return webElement;
  }
  @Step({"<key> alanına kaydır"})
  public void scrollToElement(String key) {
    scrollToElementToBeVisible(key);
  }

  @Step({"kaydır"})
  public void scrollToElementTwo() {
    executeJS("window.scrollBy(0,500)", true);

  }


  @Step({"<key> alanına js ile kaydır"})
  public void scrollToElementWithJs(String key) {
    ElementInfo elementInfo = StoreHelper.INSTANCE.findElementInfoByKey(key);
    WebElement element = driver.findElement(ElementHelper.getElementInfoToBy(elementInfo));
    ((JavascriptExecutor) driver).executeScript("arguments[0].scrollIntoView(true);", element);
  }


  @Step({"<length> uzunlugunda random bir kelime üret ve <saveKey> olarak sakla"})
  public void createRandomString(int length, String saveKey) {
    StoreHelper.INSTANCE.saveValue(saveKey,  randomString(length ));
  }



  @Step({"<key> li elementi bul ve değerini <saveKey> saklanan degeri yazdir",
          "Find element by <key> and compare saved key <saveKey>"})
  public void equalsSendTextByKey(String key, String saveKey) throws InterruptedException {
    WebElement element = null;
    int waitVar = 0;
    element = findElementWithKey(key);
    while (true) {
      if (element.isDisplayed()) {
        logger.info("WebElement is found at: " + waitVar + " second.");
        element.clear();
        StoreHelper.INSTANCE.getValue(saveKey);
        element.sendKeys(StoreHelper.INSTANCE.getValue(saveKey));

        break;
      } else {
        waitVar = waitVar + 1;
        Thread.sleep(1000);
        if (waitVar == 20) {
          throw new NullPointerException(String.format("by = %s Web element list not found"));
        } else {
        }
      }
    }
  }

  private Long getTimestamp() {
    Timestamp timestamp = new Timestamp(System.currentTimeMillis());
    return (timestamp.getTime());
  }
  @Step({"<key> li elementi bul, temizle ve rasgele  email değerini yaz",
          "Find element by <key> clear and send keys  random email"})
  public void RandomeMail(String key){
    Long timestamp = getTimestamp();
    WebElement webElement = findElementWithKey(key);
    webElement.clear();
    webElement.sendKeys("otomasyontest" + timestamp + "@testinium.com");

  }

  @Step({"<key> li elementi bul, temizle ve rasgele isim değerini yaz",
          "Find element by <key> clear and send keys random isim"})
  public void RandomeName(String key){
    Long timestamp = getTimestamp();
    WebElement webElement = findElementWithKey(key);
    webElement.clear();
    webElement.sendKeys("testotomasyon" + timestamp + "@testinium.com");

  }


  @Step({"<key> li elementi bul ve değerini <saveKey> olarak sakla",
          "Find element by <key> and save text <saveKey>"})
  public void saveTextByKey(String key, String saveKey) throws InterruptedException {
    Thread.sleep(1000);
    StoreHelper.INSTANCE.saveValue(saveKey, findElementWithKey(key).getText());
    Thread.sleep(2000);

  }
  @Step({"<key> li elementi bul ve değerini <saveKey> saklanan değeri içeriyor mu kontrol et",
          "Find element by <key> and compare saved key <saveKey>"})
  public void equalsSaveTextByKeyContain(String key, String saveKey) {
    Assert.assertTrue(StoreHelper.INSTANCE.getValue(saveKey).contains(findElementWithKey(key).getText()));
  }


  @Step({"<key> li elementi bul ve değerini <saveKey> saklanan değer ile karşılaştır ve değişiklik oldugunu dogrula",
          "Find element by <key> and compare saved key <saveKey>"})
  public void equalsSaveTextByKeyNotequal(String key, String saveKey) {
    Assert.assertNotEquals(StoreHelper.INSTANCE.getValue(saveKey), findElementWithKey(key).getText());
  }

  @Step({"<key> li elementi bul, temizle ve <text> değerini yaz",
          "Find element by <key> clear and send keys <text>"})
  public void sendKeysByKey(String key, String text) {

    WebElement webElement = findElementWithKey(key);
    webElement.clear();
    webElement.sendKeys(text);
  }

  @Step({"<key> li elementi bul, temizle",
          "Find element by <key> clear "})
  public void sendKeysByKey2(String key) {
    WebElement webElement = findElementWithKey(key);
    webElement.clear();
  }

  @Step({"<key> li elementi bul ve değerini <saveKey> saklanan değer ile karşılaştır",
          "Find element by <key> and compare saved key <saveKey>"})
  public void equalsSaveTextByKey(String key, String saveKey) {
    Assert.assertEquals(StoreHelper.INSTANCE.getValue(saveKey), findElementWithKey(key).getText());
  }

  public String randomName(int stringLength){
    Random random = new Random();
    char[] chars = "ABCDEFGHIJKLMNOPQRSTUWVXYZabcdefghijklmnopqrstuwvxyz".toCharArray();
    String stringRandom = "";
    for (int i = 0; i < stringLength; i++) {
      stringRandom = stringRandom + String.valueOf(chars[random.nextInt(chars.length)]);
    }
    return stringRandom;
  }
  @Step({"<key> elementine random isim yaz"})
  public void writeRandomNameToElement(String key){
    findElement(key).sendKeys(randomName(3));
  }

  @Step({"<key> li elementin değeri <text> e eşitliğini kontrol et",
          "Find element by <key> and text equals <text>"})
  public void equalsTextByKey(String key, String text) {
    Assert.assertEquals(text, findElementWithKey(key).getText());
  }

  @Step({"Elementin yüklenmesini bekle ve tıkla <key>"})
  public WebElement getElementWithKeyIfExists2(String key){
    WebElement webElement;
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      try {
        webElement = findElementWithKey(key);
        logger.info(key + " elementi bulundu.");
        actions.moveToElement(findElement(key));
        actions.click();
        actions.build().perform();
        logger.info(key + " elementine focus ile tıklandı.");
        return webElement;
      } catch (WebDriverException e) {
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element: '" + key + "' doesn't exist.");
    return null;
  }

  @Step("<key> li tarihten iki gün sonraki tarihi seç")
  public void tarihBelirle(String key){
    waitElementLoadByKey(key);
    String dateNow = findElementWithKey(key).getText();
    int date = Integer.parseInt(dateNow);
    date= date+2;
    WebElement webElement = driver.findElement(By.xpath("//div[@role='option'][@aria-label='day-"+date+"']"));
    webElement.click();
  }

  public WebElement waitElementLoadByKey(String key) {
    WebElement webElement;
    int loopCount = 0;
    while (loopCount < DEFAULT_MAX_ITERATION_COUNT) {
      try {
        webElement = findElement(key);
        System.out.println("Element:'" + key + "' found.");
        return webElement;
      } catch (Exception e) {
      }
      loopCount++;
      waitByMilliSeconds(DEFAULT_MILLISECOND_WAIT_AMOUNT);
    }
    Assert.fail("Element: '" + key + "' doesn't exist.");
    return null;
  }

  @Step("<key> li Textbox'ı temizle ve text değerini <text> yaz")
  public void Temizle(String key, String text) throws InterruptedException {
    for(int i=0;i<15;i++){

      findElementWithKey(key).sendKeys(BACK_SPACE);

    }
    waitBySeconds(1);
    sendKeysByKey(key, text);
  }

  @Step({"Check element <key> is not clickable"
  ,"Elementinin <key> tıklanabilirliğini kontrol et"})
  public void checkElementIsNotClickable(String key){
    WebElement webElement = findElementWithKey(key);
    try {
      webElement.click();
    } catch (ElementClickInterceptedException e) {
      logger.info("Element: '" + key + "' tıklanabilir değil");
      return;
    }
    Assert.fail("Element '" + key + "' tıklanabilir.");
  }

  @Step({"<key> li elementi bul ve varsa dokun", "Click element by <key> if exist"})
  public void existTapByKey(String key) {

    WebElement element = null;
    try {
      element = findElementWithKey(key);
    } catch (Exception e) {
      e.printStackTrace();
    }
    if (element != null) {
      element.click();
    }
  }

  public static String randomNum(int stringLength) {
    Random random = new Random();
    char[] chars = "1234567890".toCharArray();
    String stringRandom = "";
    for (int i = 0; i < stringLength; i++) {
      stringRandom = stringRandom + String.valueOf(chars[random.nextInt(chars.length)]);
    }
    return stringRandom;
  }

  @Step("<key> li elementine random telefon numarası yaz")
  public void randomTel(String key){

    String phoneNum = "93"+randomNum(7);
    findElementWithKey(key).sendKeys(phoneNum);

  }

  @Step("<text> servis tipi kontrolü yapılır")
  public void serviceTypeControl(String text){
    switch (text){
      case "GelAl":
        waitBySeconds(2);
        if(driver.findElements(By.xpath("//span[contains(text(),'Adrese Teslim')]")).size() > 0) {
          getElementWithKeyIfExists("anasayfaServisTipiDegisimibuton");
          clickElement("anasayfaServisTipiDegisimibuton");
          getElementWithKeyIfExists("gelAlButon");
          clickElement("gelAlButon");

          if(findElements("ilDropdownGelAl").size() > 0){
            waitBySeconds(2);
            getElementWithKeyIfExists("ilDropdownGelAl");
            clickElement("ilDropdownGelAl");
            getElementWithKeyIfExists("ilİstanbul");
            clickElement("ilİstanbul");
            waitBySeconds(2);
            getElementWithKeyIfExists("ilceDropdownGelAl");
            clickElement("ilceDropdownGelAl");
            getElementWithKeyIfExists("ilceAdalar");
            clickElement("ilceAdalar");
            waitBySeconds(4);
            getElementWithKeyIfExists("mahalleDropdownGelAl");
            clickElement("mahalleDropdownGelAl");
            getElementWithKeyIfExists("mahalleBurgazadaMahallesi");
            clickElement("mahalleBurgazadaMahallesi");
            waitBySeconds(4);
            getElementWithKeyIfExists("acikSubeleriGoster");
            clickElement("acikSubeleriGoster");
            getElementWithKeyIfExists("subeleriGosterButon");
            clickElement("subeleriGosterButon");
            getElementWithKeyIfExists("ilkSubeSecimi");
            clickElement("ilkSubeSecimi");
            waitBySeconds(2);
            getElementWithKeyIfExists("seciliSubeIleDevamEtButon");
            clickElement("seciliSubeIleDevamEtButon");
            waitBySeconds(3);

            if(findElements("cookiesKapatButon").size() > 0) {
              getElementWithKeyIfExists("cookiesKapatButon");
              clickElement("cookiesKapatButon");
              waitBySeconds(4);
            }
          }
          else if (findElements("seciliAdresIleDevamEtButonilkadres").size() > 0) {
            if(findElements("cookiesKapatButon").size() > 0) {
              getElementWithKeyIfExists("cookiesKapatButon");
              clickElement("cookiesKapatButon");
              waitBySeconds(4);

            }
            getElementWithKeyIfExists("seciliAdresIleDevamEtButonilkadres");
            clickElement("seciliAdresIleDevamEtButonilkadres");
            waitBySeconds(4);
            getElementWithKeyIfExists("siparisSayfasiSeciliAdresIleDevamEtButon");
            clickElement("siparisSayfasiSeciliAdresIleDevamEtButon");
            waitBySeconds(1);
          }
        }

        else {
          logger.info("Kullanıcı Gel Al Servis Tipinde!!");
        }

        break;
      case "AdreseTeslim":
        waitBySeconds(2);
        if(driver.findElements(By.xpath("//span[contains(text(),'Gel Al')]")).size() > 0)
        {
          getElementWithKeyIfExists("anasayfaServisTipiDegisimibuton");
          clickElement("anasayfaServisTipiDegisimibuton");
          waitBySeconds(4);
          getElementWithKeyIfExists("adreseTeslimButon");
          clickElement("adreseTeslimButon");
          waitBySeconds(4);
          if (findElements("ilDropdown").size() > 0) {
            getElementWithKeyIfExists("ilDropdown");
            clickElement("ilDropdown");
            waitBySeconds(4);
            getElementWithKeyIfExists("ilİstanbul");
            clickElement("ilİstanbul");
            waitBySeconds(4);
            getElementWithKeyIfExists("ilceDropdown");
            clickElement("ilceDropdown");
            waitBySeconds(4);
            getElementWithKeyIfExists("ilceAdalar");
            clickElement("ilceAdalar");
            waitBySeconds(4);

            try {
              clickElement("mahalleDropdown");
            } catch (Exception e){
              logger.info("Mahalle Dropdown Secildi");
            }
            waitBySeconds(4);
            try {
              clickElement("mahalleBurgazadaMahallesi");
            } catch (Exception e){
              logger.info("Mahalle Secildi");
            }
            waitBySeconds(4);
            try {
              clickElement("caddeDropdownid");
            } catch (Exception e){
              logger.info("Cadde dropdown Secildi");
            }
            waitBySeconds(4);
            try {
              clickElement("caddeBurgazCayırıSk");
            } catch (Exception e){
              logger.info("Cadde Secildi");
            }
            waitBySeconds(4);
            try {
              clickElement("apartmanNoid");
            } catch (Exception e){
              logger.info("Apartman Dropdown Secildi");
            }
            waitBySeconds(4);
            try {
              clickElement("apartmanNoUc");
            } catch (Exception e){
              logger.info("Apartman Secildi");
            }
            waitBySeconds(4);
            getElementWithKeyIfExists("seciliAdresIleDevamEtButon");
            clickElement("seciliAdresIleDevamEtButon");

            if(findElements("cookiesKapatButon").size() > 0) {
              getElementWithKeyIfExists("cookiesKapatButon");
              clickElement("cookiesKapatButon");
              waitBySeconds(4);
            }
          }
          else if (findElements("seciliAdresIleDevamEtButonilkadres").size() > 0) {
            if(findElements("cookiesKapatButon").size() > 0) {
              getElementWithKeyIfExists("cookiesKapatButon");
              clickElement("cookiesKapatButon");
              waitBySeconds(4);
            }
            //getElementWithKeyIfExists("seciliAdresIleDevamEtButonilkadres");
            //clickElement("seciliAdresIleDevamEtButonilkadres");
            //waitBySeconds(4);
            getElementWithKeyIfExists("siparisSayfasiSeciliAdresIleDevamEtButon");
            clickElement("siparisSayfasiSeciliAdresIleDevamEtButon");
            waitBySeconds(1);
          }
        }
        else {
          logger.info("Kullanıcı Adrese Teslim Servis Tipinde!!");
        }
        break;
      default:
        break;
    }
  }


  @Step("<key> servis tipi seçilir ve adres seçimi yapılır")
  public void choiceServiceType(String key) {
      waitBySeconds(4);
    if (findElements(key).size()>0) {
      findElements(key);
      getElementWithKeyIfExists(key);
      clickElement(key);
      waitBySeconds(2);

      //Gel Al
      if (findElements("acikSubeleriGoster").size() > 0) {
        getElementWithKeyIfExists("ilDropdownGelAl");
        clickElement("ilDropdownGelAl");
        getElementWithKeyIfExists("ilİstanbul");
        clickElement("ilİstanbul");
        waitBySeconds(2);
        getElementWithKeyIfExists("ilceDropdownGelAl");
        clickElement("ilceDropdownGelAl");
        getElementWithKeyIfExists("ilceAdalar");
        clickElement("ilceAdalar");
        waitBySeconds(4);
        getElementWithKeyIfExists("mahalleDropdownGelAl");
        clickElement("mahalleDropdownGelAl");
        getElementWithKeyIfExists("mahalleBurgazadaMahallesi");
        clickElement("mahalleBurgazadaMahallesi");
        waitBySeconds(4);
        getElementWithKeyIfExists("acikSubeleriGoster");
        clickElement("acikSubeleriGoster");
        getElementWithKeyIfExists("subeleriGosterButon");
        clickElement("subeleriGosterButon");
        getElementWithKeyIfExists("ilkSubeSecimi");
        clickElement("ilkSubeSecimi");
        waitBySeconds(2);
        getElementWithKeyIfExists("seciliSubeIleDevamEtButon");
        clickElement("seciliSubeIleDevamEtButon");
        waitBySeconds(3);
        if(findElements("cookiesKapatButon").size() > 0) {
          getElementWithKeyIfExists("cookiesKapatButon");
          clickElement("cookiesKapatButon");
          waitBySeconds(4);
        }
      }
      //Kayıtlı Adres Çıkarsa
      else if (findElements("seciliAdresIleDevamEtButonilkadres").size() > 0) {
        if(findElements("cookiesKapatButon").size() > 0) {
          getElementWithKeyIfExists("cookiesKapatButon");
          clickElement("cookiesKapatButon");
          waitBySeconds(4);
        }
        //getElementWithKeyIfExists("seciliAdresIleDevamEtButonilkadres");
        //clickElement("seciliAdresIleDevamEtButonilkadres");
        //waitBySeconds(4);
        getElementWithKeyIfExists("siparisSayfasiSeciliAdresIleDevamEtButon");
        clickElement("siparisSayfasiSeciliAdresIleDevamEtButon");
        waitBySeconds(4);

      }
      //Adrese Teslim
      else if (findElements("acikSubeleriGoster").size() <= 0) {
        waitBySeconds(2);
        getElementWithKeyIfExists("ilDropdown");
        clickElement("ilDropdown");
        waitBySeconds(4);
        getElementWithKeyIfExists("ilİstanbul");
        clickElement("ilİstanbul");
        waitBySeconds(4);
        getElementWithKeyIfExists("ilceDropdown");
        clickElement("ilceDropdown");
        waitBySeconds(4);
        getElementWithKeyIfExists("ilceAdalar");
        clickElement("ilceAdalar");
        waitBySeconds(4);

        try {
          clickElement("mahalleDropdown");
        } catch (Exception e){
          logger.info("Mahalle Dropdown Secildi");
        }
        waitBySeconds(4);
        try {
          clickElement("mahalleBurgazadaMahallesi");
        } catch (Exception e){
          logger.info("Mahalle Secildi");
        }
        waitBySeconds(4);
        try {
          clickElement("caddeDropdownid");
        } catch (Exception e){
          logger.info("Cadde dropdown Secildi");
        }
        waitBySeconds(4);
        try {
          clickElement("caddeBurgazCayırıSk");
        } catch (Exception e){
          logger.info("Cadde Secildi");
        }
        waitBySeconds(4);
        try {
          clickElement("apartmanNoid");
        } catch (Exception e){
          logger.info("Apartman Dropdown Secildi");
        }
        waitBySeconds(4);
        try {
          clickElement("apartmanNoUc");
        } catch (Exception e){
          logger.info("Apartman Secildi");
        }
        waitBySeconds(4);
        getElementWithKeyIfExists("seciliAdresIleDevamEtButon");
        clickElement("seciliAdresIleDevamEtButon");
        if(findElements("cookiesKapatButon").size() > 0) {
          getElementWithKeyIfExists("cookiesKapatButon");
          clickElement("cookiesKapatButon");
          waitBySeconds(4);
        }
      }

    }
  }

  @Step("<key> Varsa adres bilgileri tamamlanır (Kapı No Manuel)")
  public void addressSelect(String key){
      waitBySeconds(4);
    if(findElements(key).size() > 0){
      logger.info("Adres tamamlanıyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("popupmahalleDropdown");
      clickElement("popupmahalleDropdown");
      waitBySeconds(2);
      getElementWithKeyIfExists("mahalleBurgazadaMahallesi");
      clickElement("mahalleBurgazadaMahallesi");
      waitBySeconds(2);
      getElementWithKeyIfExists("caddeDropdown");
      clickElement("caddeDropdown");
      waitBySeconds(2);
      getElementWithKeyIfExists("caddeSokakDropdown835Sokak");
      clickElement("caddeSokakDropdown835Sokak");
      waitBySeconds(2);
      getElementWithKeyIfExists("kapiNoTextbox");
      clickElement("kapiNoTextbox");
      waitBySeconds(2);
      sendKeysByKey("kapiNoTextbox","2");
      getElementWithKeyIfExists("daireTextbox");
      clickElement("daireTextbox");
      waitBySeconds(2);
      sendKeysByKey("daireTextbox","1");
      getElementWithKeyIfExists("adresAdiTextbox");
      clickElement("adresAdiTextbox");
      waitBySeconds(2);
      sendKeysByKey("adresAdiTextbox","test");
      getElementWithKeyIfExists("adresSayfasiTelefonTextbox");
      clickElement("adresSayfasiTelefonTextbox");
      waitBySeconds(2);
      sendKeys("923456789","adresSayfasiTelefonTextbox");
      sendKeysByKey("adresTarifiTextbox","test");
      getElementWithKeyIfExists("adresKaydetButon");
      clickElement("adresKaydetButon");
      waitBySeconds(4);
      //getElementWithKeyIfExists("uyelikBilgilerimAdreslerimIlkAdres");
      //clickElement("uyelikBilgilerimAdreslerimIlkAdres");
      waitBySeconds(2);
      getElementWithKeyIfExists("siparisSayfasiSeciliAdresIleDevamEtButon");
      clickElement("siparisSayfasiSeciliAdresIleDevamEtButon");
      waitBySeconds(2);
    }
    else{
      logger.info("Ödeme sayfasına geçildi!!!");
    }
  }

  @Step("<key> Varsa adres bilgileri tamamlanır (Kapı No Manuel) Guest")
  public void addressSelectGuest(String key){
      waitBySeconds(4);
    if(findElements(key).size() > 0){
      logger.info("Adres tamamlanıyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("popupmahalleDropdown");
      clickElement("popupmahalleDropdown");
      waitBySeconds(2);
      getElementWithKeyIfExists("mahalleBurgazadaMahallesi");
      clickElement("mahalleBurgazadaMahallesi");
      waitBySeconds(2);
      getElementWithKeyIfExists("caddeDropdown");
      clickElement("caddeDropdown");
      waitBySeconds(2);
      getElementWithKeyIfExists("caddeSokakDropdown835Sokak");
      clickElement("caddeSokakDropdown835Sokak");
      waitBySeconds(2);
      getElementWithKeyIfExists("kapiNoTextbox");
      clickElement("kapiNoTextbox");
      waitBySeconds(2);
      sendKeysByKey("kapiNoTextbox","2");
      getElementWithKeyIfExists("daireTextbox");
      clickElement("daireTextbox");
      waitBySeconds(2);
      sendKeysByKey("daireTextbox","1");
      waitBySeconds(2);
      getElementWithKeyIfExists("adresSayfasiTelefonTextbox");
      clickElement("adresSayfasiTelefonTextbox");
      waitBySeconds(2);
      sendKeys("923456789","adresSayfasiTelefonTextbox");
      sendKeysByKey("adresTarifiTextbox","test");
      getElementWithKeyIfExists("adresKaydetButon");
      clickElement("adresKaydetButon");
      waitBySeconds(4);
      getElementWithKeyIfExists("uyelikBilgilerimAdreslerimIlkAdres");
      clickElement("uyelikBilgilerimAdreslerimIlkAdres");
      waitBySeconds(2);
      getElementWithKeyIfExists("siparisSayfasiSeciliAdresIleDevamEtButon");
      clickElement("siparisSayfasiSeciliAdresIleDevamEtButon");
      waitBySeconds(2);
    }
    else{
      logger.info("Ödeme sayfasına geçildi!!!");
    }
  }

  @Step("Kampanya urun secimi yapılır")
  public void kampanyaSec(){
    waitBySeconds(5);
    if(findElements("birinciUrunSeciniz").size() > 0){
      logger.info("Kampanya 1. ürün seçiliyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("birinciUrunSeciniz");
      clickElement("birinciUrunSeciniz");
      waitBySeconds(2);
      getElementWithKeyIfExists("birinciUrunBirinciPizzaSec");
      clickElement("birinciUrunBirinciPizzaSec");
      waitBySeconds(2);

    }
    if(findElements("ikinciUrunSeciniz").size() > 0){
      logger.info("Kampanya 2. ürün seçiliyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("ikinciUrunSeciniz");
      clickElement("ikinciUrunSeciniz");
      waitBySeconds(2);
      getElementWithKeyIfExists("ikinciUrunBirinciPizzaSec");
      clickElement("ikinciUrunBirinciPizzaSec");
      waitBySeconds(2);

    }
    if(findElements("ucuncuUrunSeciniz").size() > 0){
      logger.info("Kampanya 3. ürün seçiliyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("ucuncuUrunSeciniz");
      clickElement("ucuncuUrunSeciniz");
      waitBySeconds(2);
      getElementWithKeyIfExists("ucuncuUrunBirinciPizzaSec");
      clickElement("ucuncuUrunBirinciPizzaSec");
      waitBySeconds(2);

    }
    if(findElements("dorduncuUrunSeciniz").size() > 0){
      logger.info("Kampanya 4. ürün seçiliyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("dorduncuUrunSeciniz");
      clickElement("dorduncuUrunSeciniz");
      waitBySeconds(2);
      getElementWithKeyIfExists("dorduncuUrunBirinciPizzaSec");
      clickElement("dorduncuUrunBirinciPizzaSec");
      waitBySeconds(2);

    }
    if(findElements("besinciUrunSeciniz").size() > 0){
      logger.info("Kampanya 5. ürün seçiliyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("besinciUrunSeciniz");
      clickElement("besinciUrunSeciniz");
      waitBySeconds(2);
      getElementWithKeyIfExists("besinciUrunBirinciPizzaSec");
      clickElement("besinciUrunBirinciPizzaSec");
      waitBySeconds(2);

    }if(findElements("altinciUrunSeciniz").size() > 0){
      logger.info("Kampanya 6. ürün seçiliyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("altinciUrunSeciniz");
      clickElement("altinciUrunSeciniz");
      waitBySeconds(2);
      getElementWithKeyIfExists("altinciUrunBirinciPizzaSec");
      clickElement("altinciUrunBirinciPizzaSec");
      waitBySeconds(2);

    }if(findElements("yedinciUrunSeciniz").size() > 0){
      logger.info("Kampanya 7. ürün seçiliyor!!!");
      waitBySeconds(4);
      getElementWithKeyIfExists("yedinciUrunSeciniz");
      clickElement("yedinciUrunSeciniz");
      waitBySeconds(2);
      getElementWithKeyIfExists("yedinciUrunBirinciPizzaSec");
      clickElement("yedinciUrunBirinciPizzaSec");
      waitBySeconds(2);

    }


  }

  @Step("Kayitli adres cikarsa adres sec yoksa servis tipi sec")
  public void kayitliAdres(){
    if (findElements("seciliAdresIleDevamEtButonilkadres").size() > 0) {
      if(findElements("cookiesKapatButon").size() > 0) {
        getElementWithKeyIfExists("cookiesKapatButon");
        clickElement("cookiesKapatButon");
        waitBySeconds(4);
      }
      getElementWithKeyIfExists("seciliAdresIleDevamEtButonilkadres");
      clickElement("seciliAdresIleDevamEtButonilkadres");
      waitBySeconds(4);
      getElementWithKeyIfExists("siparisSayfasiSeciliAdresIleDevamEtButon");
      clickElement("siparisSayfasiSeciliAdresIleDevamEtButon");
      waitBySeconds(4);

    }
    else if (findElements("acikSubeleriGoster").size() <= 0) {
      waitBySeconds(2);
      getElementWithKeyIfExists("ilDropdown");
      clickElement("ilDropdown");
      waitBySeconds(4);
      getElementWithKeyIfExists("ilİstanbul");
      clickElement("ilİstanbul");
      waitBySeconds(4);
      getElementWithKeyIfExists("ilceDropdown");
      clickElement("ilceDropdown");
      waitBySeconds(4);
      getElementWithKeyIfExists("ilceAdalar");
      clickElement("ilceAdalar");
      waitBySeconds(4);

      try {
        clickElement("mahalleDropdown");
      } catch (Exception e){
        logger.info("Mahalle Dropdown Secildi");
      }
      waitBySeconds(4);
      try {
        clickElement("mahalleBurgazadaMahallesi");
      } catch (Exception e){
        logger.info("Mahalle Secildi");
      }
      waitBySeconds(4);
      try {
        clickElement("caddeDropdownid");
      } catch (Exception e){
        logger.info("Cadde dropdown Secildi");
      }
      waitBySeconds(4);
      try {
        clickElement("caddeBurgazCayırıSk");
      } catch (Exception e){
        logger.info("Cadde Secildi");
      }
      waitBySeconds(4);
      getElementWithKeyIfExists("seciliAdresIleDevamEtButon");
      clickElement("seciliAdresIleDevamEtButon");
    }

    else if (findElements("acikSubeleriGoster").size() > 0) {
      getElementWithKeyIfExists("ilDropdownGelAl");
      clickElement("ilDropdownGelAl");
      getElementWithKeyIfExists("ilİstanbul");
      clickElement("ilİstanbul");
      waitBySeconds(2);
      getElementWithKeyIfExists("ilceDropdownGelAl");
      clickElement("ilceDropdownGelAl");
      getElementWithKeyIfExists("ilceAdalar");
      clickElement("ilceAdalar");
      waitBySeconds(4);
      getElementWithKeyIfExists("mahalleDropdownGelAl");
      clickElement("mahalleDropdownGelAl");
      getElementWithKeyIfExists("mahalleBurgazadaMahallesi");
      clickElement("mahalleBurgazadaMahallesi");
      waitBySeconds(4);
      getElementWithKeyIfExists("acikSubeleriGoster");
      clickElement("acikSubeleriGoster");
      getElementWithKeyIfExists("subeleriGosterButon");
      clickElement("subeleriGosterButon");
      getElementWithKeyIfExists("ilkSubeSecimi");
      clickElement("ilkSubeSecimi");
      waitBySeconds(2);
      getElementWithKeyIfExists("seciliSubeIleDevamEtButon");
      clickElement("seciliSubeIleDevamEtButon");
      waitBySeconds(3);
      if(findElements("cookiesKapatButon").size() > 0) {
        getElementWithKeyIfExists("cookiesKapatButon");
        clickElement("cookiesKapatButon");
        waitBySeconds(4);
      }
    }
  }

  @Step("Pizza sepete eklenir veya kampanyayali ürün sepete eklenir")
  public void pizzaAndCampaignSelection() {
    waitBySeconds(5);
    if (findElements("kampanyaliUrunlereGitButton").size() > 0) {
      logger.info("Kampanyalı ürünlere gidiliyor");
      waitBySeconds(4);
      getElementWithKeyIfExists("kampanyaliUrunlereGitButton");
      clickElement("kampanyaliUrunlereGitButton");
      waitBySeconds(2);
      getElementWithKeyIfExists("ilkKampanyaSec");
      clickElement("ilkKampanyaSec");
      waitBySeconds(2);
      kampanyaSec();
      waitBySeconds(2);
      getElementWithKeyIfExists("firsatSepetEkle");
      clickElement("firsatSepetEkle");
      waitBySeconds(10);
      existTapByKey("sepeteUrunEkledenSonraYeKazanPopupKapatButon");

    }
    if (findElements("pizzaSepeteEkle").size() > 0) {
      logger.info("Pizza sepete ekleniyor");
      waitBySeconds(4);
      getElementWithKeyIfExists("pizzaSepeteEkle");
      clickElement("pizzaSepeteEkle");
      waitBySeconds(10);
      existTapByKey("sepeteUrunEkledenSonraYeKazanPopupKapatButon");

    }
  }
  @Step("<text> Giris dizayn secimi yapilir")
  public void girisDizaynSecimi(String text) {
    waitBySeconds(5);
    if (findElements("adreseTeslimButon").size() > 0) {
      logger.info("Eski Dizayna gidiliyor");
      switch (text) {
        case "girisYap":
          waitBySeconds(2);
          getElementWithKeyIfExists("loginButton");
          clickElement("loginButton");
          break;
        case "UyeOl":
          waitBySeconds(2);
          getElementWithKeyIfExists("uyeOlButon");
          clickElement("uyeOlButon");
          break;
      }
    }
     else {
      logger.info("Yeni dizayna gidiliyor");
      waitBySeconds(4);
      switch (text) {
        case "girisYap":
          waitBySeconds(2);
          getElementWithKeyIfExists("loginButton");
          clickElement("loginButton");
          break;
        case "UyeOl":
          waitBySeconds(2);
          getElementWithKeyIfExists("uyeOlButon");
          clickElement("uyeOlButon");
          break;
      }
  }
  }
  @Step("<text> adrese teslim - Gal al dizayn secimi")
  public void uyeOlmadanDizaynSecimi(String text) {
    waitBySeconds(5);
    if (findElements("adreseTeslimButon").size() > 0) {
      logger.info("Eski dizayn uyeliksiz gidiliyor");
      switch (text) {
        case "AdreseTeslim":
          waitBySeconds(2);
          getElementWithKeyIfExists("adreseTeslimButon");
          clickElement("adreseTeslimButon");
          break;
        case "GelAl":
          waitBySeconds(2);
          getElementWithKeyIfExists("gelAlButon");
          clickElement("gelAlButon");
          break;
      }
    }
    else {
      logger.info("Yeni dizayna uyeliksiz gidiliyor");
      waitBySeconds(4);
      getElementWithKeyIfExists("uyeOlmadanDevamEtButtonXpath");
      clickElement("uyeOlmadanDevamEtButtonXpath");
      waitBySeconds(4);
      switch (text) {
        case "AdreseTeslim":
          waitBySeconds(2);
          getElementWithKeyIfExists("adreseTeslimButon");
          clickElement("adreseTeslimButon");
          break;
        case "GelAl":
          waitBySeconds(2);
          getElementWithKeyIfExists("gelAlButon");
          clickElement("gelAlButon");
          break;
      }
    }

  }


  @Step("Telefon dogrulama kodu girilir")
  public void otpTarihFormati() {
    LocalDateTime now = LocalDateTime.now();
    DateTimeFormatter format = DateTimeFormatter.ofPattern("MMddHH");
    String formatDateTime = now.format(format);
    int formatDateTimeInt = Integer.parseInt(formatDateTime);
    int newDateTimeInt = formatDateTimeInt + 3;
    String newDateTime = String.valueOf("0" + newDateTimeInt);
    logger.info(formatDateTime);
    System.out.println(formatDateTimeInt);
    logger.info(newDateTime);
    getElementWithKeyIfExists("otpInput1");
    clickElement("otpInput1");
    WebElement webElement = findElementWithKey("otpInput1");
    webElement.clear();
    webElement.sendKeys(newDateTime);
  }

}



