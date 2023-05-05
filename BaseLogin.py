import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from InputanRepository.DataInputan import GlobalVariables
from ObjectRepository.All_Object import register_elem
from ObjectRepository.All_Object import login_elem


def test_login(driver, self):
        driver.implicitly_wait(10)
        driver.get(GlobalVariables.BaseUrl)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-login").click()

        #validate login URL
        url = driver.current_url
        self.assertEqual(url, GlobalVariables.BaseUrl + "login")
        assert driver.find_element(By.XPATH, "//h1[text() = 'Welcome, Please Sign In!']").is_displayed()    
        #input valid email & password
        driver.find_element(By.ID, register_elem.email_txt).send_keys(GlobalVariables.valid_email)
        driver.find_element(By.ID, register_elem.password_txt).send_keys(GlobalVariables.valid_psw)
        driver.find_element(By.XPATH, login_elem.login_btn).click()

 