import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from InputanRepository.DataInputan import GlobalVariables
from ObjectRepository.All_Object import register_elem

class demowebshop(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_register(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(GlobalVariables.BaseUrl)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-register").click()

        #validate registration URL
        url = driver.current_url
        self.assertEqual(url, GlobalVariables.BaseUrl + "register")
        assert driver.find_element(By.XPATH,"//h1[text() = 'Register' ]").is_displayed()
       
        #validate mandatory data
        driver.find_element(By.ID, register_elem.register_btn).click()
        data = driver.find_element(By.XPATH, register_elem.firstname_error_msg).text
        self.assertIn("First name is required.", data) 
        data = driver.find_element(By.XPATH, register_elem.lastname_error_msg).text
        self.assertIn("Last name is required.", data) 
        data = driver.find_element(By.XPATH, register_elem.email_eror_msg).text
        self.assertIn("Email is required.", data) 
        data = driver.find_element(By.XPATH, register_elem.password_error_msg).text
        self.assertIn("Password is required.", data)
        data = driver.find_element(By.XPATH, register_elem.confirmPassword_error_msg).text
        self.assertIn("Password is required.", data)

        #Input mandatory data
        driver.find_element(By.ID, register_elem.genderFemale_btn).click()
        driver.find_element(By.ID, register_elem.firstname_txt).send_keys(GlobalVariables.firstname)
        driver.find_element(By.ID, register_elem.lastname_txt).send_keys(GlobalVariables.lastname)
        driver.find_element(By.ID, register_elem.email_txt).send_keys(GlobalVariables.valid_email)

        #validate password must 6 characters
        driver.find_element(By.ID, register_elem.password_txt).send_keys(GlobalVariables.invalid_psw)
        data = driver.find_element(By.XPATH, register_elem.password_error_msg).text
        self.assertIn("The password should have at least 6 characters.", data)

        #input valid password
        driver.find_element(By.ID, register_elem.password_txt).send_keys(GlobalVariables.valid_psw)

        #password & confirm password do not match
        driver.find_element(By.ID, register_elem.confirmPassword_txt).send_keys(GlobalVariables.invalid_psw)
        data = driver.find_element(By.XPATH, register_elem.confirmPassword_error_msg).text
        self.assertIn("The password and confirmation password do not match.", data)
        
        #input valid confirm password
        driver.find_element(By.ID, register_elem.confirmPassword_txt).send_keys(GlobalVariables.valid_confirm_psw)
        driver.find_element(By.ID, register_elem.register_btn).click()          
        

        #validate account info
        data = driver.find_element(By.CLASS_NAME, "account").text
        self.assertIn(GlobalVariables.valid_email, data)
        data = driver.find_element(By.CLASS_NAME, "result").text
        self.assertIn("Your registration completed", data)

        #validate after registered and click continue btn back to main page
        driver.find_element(By.XPATH, "//input[@class='button-1 register-continue-button']").click()
        url2 = driver.current_url
        self.assertEqual(url2, GlobalVariables.BaseUrl)

    def test_register_with_existing_email (self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get(GlobalVariables.BaseUrl)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "ico-register").click()

        #Input mandatory data
        driver.find_element(By.ID, register_elem.genderFemale_btn).click()
        driver.find_element(By.ID, register_elem.firstname_txt).send_keys(GlobalVariables.firstname)
        driver.find_element(By.ID, register_elem.lastname_txt).send_keys(GlobalVariables.lastname)
        driver.find_element(By.ID, register_elem.email_txt).send_keys(GlobalVariables.existing_email)
        driver.find_element(By.ID, register_elem.password_txt).send_keys(GlobalVariables.valid_psw)
        driver.find_element(By.ID, register_elem.confirmPassword_txt).send_keys(GlobalVariables.valid_confirm_psw)
        driver.find_element(By.ID, register_elem.register_btn).click()

        #validate error msg for existing email
        data = driver.find_element(By.XPATH, register_elem.existing_email_error_msg).text
        self.assertIn("The specified email already exists", data)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()