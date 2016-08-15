package com.example.tests;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.testng.annotations.*;
import static org.testng.Assert.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class TestWeb {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @BeforeClass(alwaysRun = true)
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "https://search.yahoo.com/";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testWeb() throws Exception {
    driver.get(baseUrl + "/yhs/search?p=yahoo&ei=UTF-8&hspart=mozilla&hsimp=yhs-002");
    driver.findElement(By.id("yui_3_10_0_1_1470986686727_277")).click();
    driver.findElement(By.xpath("//ul[@id='Stream']/li/div/div/div/a/div/div/h2")).click();
    driver.findElement(By.linkText("News")).click();
    driver.findElement(By.xpath("//div[@id='tgtm-Nav-0-NavLite']/div/div[3]/div/div/ul/li[6]/a/span")).click();
    driver.findElement(By.xpath("//li[@id='uh-tb-home']/a/div/b")).click();
    driver.findElement(By.xpath("//ul[@id='Stream']/li[6]/div/div/div[2]/div/h3/a/u")).click();
  }

  @AfterClass(alwaysRun = true)
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
