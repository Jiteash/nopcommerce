from selenium import webdriver
import time
import pytest
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUseremail()
    password= ReadConfig.getPassword()

    logger= LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("******Test_001_Login********")
        self.logger.info("******Verifying Home Page Title*******")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*****Home page Title Passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*****Home page Title Failed ***")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.logger.info("******Verifyinng Login Test ***")
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        #time.sleep(5)
        self.lp.setPassword(self.password)
        #time.sleep(5)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****Login Test is  Passed ***")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.logger.warning("*****Home page Title Failed ***")
            self.driver.close()
            assert False
