from selenium import webdriver
import time
import pytest
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutils


class Test_002_DDT_Login:

    baseURL= ReadConfig.getApplicationURL()
    path= ".//TestData/LoginData.xlsx"

    logger= LogGen.loggen()


    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**** Test_002-DDT_Login ****")
        self.logger.info("******Verifyinng Login Test ***")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows=XLutils.getRowCount(self.path,'Sheet1')
        print ("Number of rows",self.rows)

        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLutils.readData(self.path,'Sheet1',r,1)
            self.password= XLutils.readData(self.path,'Sheet1',r,2)
            self.exp= XLutils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title= "Dashboard / nopCommerce administration"

            time.sleep(5)
            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("** Passed **")
                    self.lp.clickLogout()
                    lst_status.append("pass")

                elif self.exp=="fail":
                    self.logger.info("** Failed **")
                    self.lp.clickLogout();
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp == "pass":
                    self.logger.info("** failed ***")
                    lst_status.append("Fail")

                elif self.exp == "Fail":
                    self.logger.info("** Passed **")
                    lst_status.append("pass")

        if "Fail" not in lst_status:
            self.logger.info("*****Login DDT test passed*******")
            self.driver.close
            assert True
        else:
            self.logger.info("*****Login DDT test Failed*******")
            self.driver.close
            assert False

        self.logger.info("*********** End of Login DDT Test ***********")
        self.logger.info("************* Completed TC_loginDDT_002 ****** ");



