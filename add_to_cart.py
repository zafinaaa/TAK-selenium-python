import unittest
from requests import options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import BaseLogin
from InputanRepository.DataInputan import GlobalVariables
from ObjectRepository.All_Object import product_elem
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class add_to_cart_and_checkout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        

    def test_success_add_product_to_cart(self):
        driver = self.driver
        driver.implicitly_wait(15)
        BaseLogin.test_login(driver, self)
        url = self.driver.current_url
        self.assertEqual(url, GlobalVariables.BaseUrl)
        data = self.driver.find_element(By.CLASS_NAME, "account").text
        self.assertIn(GlobalVariables.valid_email, data)
       
        #hover menu computers > desktop
        hoverable = driver.find_element(By.XPATH, product_elem.computers_prd_menu)
        ActionChains(driver)\
        .move_to_element(hoverable)\
        .perform()
        
        driver.find_element(By.XPATH, product_elem.desktop_prd_sub_menu).click()
        title = self.driver.find_element(By.XPATH, product_elem.menu_title).text
        self.assertIn("Desktops", title)
        
        #scroll to element
        element = driver.find_element(By.XPATH, product_elem.computer_item)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        
        #open detail product > add to cart
        driver.find_element(By.XPATH, product_elem.computer_item).click()
        url2 = driver.current_url
        self.assertEqual(url2, GlobalVariables.BaseUrl + "build-your-cheap-own-computer")

        #select specification of product
        driver.find_element(By.ID, "product_attribute_72_5_18_65").click()
        driver.find_element(By.ID, "product_attribute_72_6_19_55").click()
        driver.find_element(By.ID, "product_attribute_72_3_20_58").click() 
        driver.find_element(By.ID, "product_attribute_72_8_30_93").click()
        #scroll to element
        element2 = driver.find_element(By.ID, "product_attribute_72_8_30_93")
        actions = ActionChains(driver)
        actions.move_to_element(element2).perform()

        #hapus default value
        driver.find_element(By.ID, product_elem.qty_txt).clear()

        #input qty dgn tidak input integer positive
        driver.find_element(By.ID, product_elem.qty_txt).send_keys(GlobalVariables.invalid_qty_product + Keys.ENTER)

        #validate error msg
        msg = driver.find_element(By.CSS_SELECTOR, ".content").text
        self.assertIn("Quantity should be positive", msg)

        time.sleep(3)

        #hapus default value
        driver.find_element(By.ID, product_elem.qty_txt).clear()
                
        #input qty dgn input integer positive
        driver.find_element(By.ID, product_elem.qty_txt).send_keys(GlobalVariables.valid_qty_product)
        
        #click add to cart button
        driver.find_element(By.ID, product_elem.add_to_cart_btn).click()

        time.sleep(3)

        data = driver.find_element(By.CSS_SELECTOR, ".content").text
        self.assertIn("The product has been added to your", data)
        
        qty_cart = self.driver.find_element(By.CLASS_NAME, product_elem.qty_cart_elem).text
        self.assertIn("(2)", qty_cart)

        time.sleep(2)

        #Go to cart
        driver.find_element(By.CLASS_NAME, product_elem.qty_cart_elem).click()

        #Validate URL
        url3 = driver.current_url
        self.assertEqual(url3, GlobalVariables.BaseUrl + "cart")

        data1 = driver.find_element(By.CLASS_NAME, "product-name").text
        self.assertIn("Build your own cheap computer", data1)

        driver.find_element(By.ID, product_elem.termsofservice).click()
        driver.find_element(By.ID, product_elem.checkout_btn).click()

        url4 = driver.current_url
        self.assertEqual(url4, GlobalVariables.BaseUrl + "onepagecheckout")

        #billing address
        country = Select(driver.find_element(By.ID, "BillingNewAddress_CountryId"))
        country.select_by_value('2')

        state_province = Select(driver.find_element(By.ID, "BillingNewAddress_StateProvinceId"))
        state_province.select_by_value('74')
        
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("City test")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("address 1 test")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("18992")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("08966655321")
        assert driver.find_element(By.XPATH, product_elem.continue_btn).is_displayed()
        driver.find_element(By.XPATH, product_elem.continue_btn).click()
        time.sleep(8)

        #shipping address
        driver.find_element(By.ID, "PickUpInStore").click()
        clickable = driver.find_element(By.XPATH, product_elem.continue_btn);
        clickable.click()
        
        #shipping method
        driver.find_element(By.ID, "shippingoption_2").click()
        driver.find_element(By.XPATH, product_elem.continue_btn).click()
        #payment method
        driver.find_element(By.ID, "paymentmethod_1").click()
        driver.find_element(By.XPATH, product_elem.continue_btn).click()
        #Payment Information
        driver.find_element(By.XPATH, product_elem.continue_btn).click()
        #confrim
        driver.find_element(By.XPATH, "//input[@value='Confirm']").click()

        url6 = driver.current_url
        self.assertEqual(url6, GlobalVariables.BaseUrl + "checkout" + "completed")
        data = driver.find_element(By.CSS_SELECTOR, ".title").text
        self.assertIn("Your order has been successfully processed!", data)

        qty_cart = self.driver.find_element(By.CLASS_NAME, product_elem.qty_cart_elem).text
        self.assertIn("(0)", qty_cart)

if __name__ == "__main__":
    unittest.main()