import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MagentoTest(unittest.TestCase):

 @classmethod
 def setUpClass(cls):
     """Set up the WebDriver instance before running any tests."""
     cls.driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
     cls.driver.maximize_window()
     cls.driver.get("https://magento.softwaretestingboard.com/")

 @classmethod
 def tearDownClass(cls):
     """Quit the WebDriver instance after all tests."""
     cls.driver.quit()

 def hover_element(self, element):
     """Performs a hover action on the given element."""
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()

 def scroll_into_view(self, element):
     """Scrolls the element into view to ensure it's interactable."""
     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

 def test_01_navigate_to_product_page(self):
     """Navigate to Women -> Tops -> Hoodies & Sweatshirts."""
     print("Navigating to Women -> Tops -> Hoodies & Sweatshirts")
     driver = self.driver

     # Hover on "Women" to reveal the dropdown
     women_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Women")))
     self.hover_element(women_menu)

     # Click on "Tops"
     tops_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tops")))
     tops_menu.click()
     time.sleep(2)

     # Scroll to "Category" and expand it
     category_filter = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//div[text()='Category']"))
     )
     self.scroll_into_view(category_filter)
     category_filter.click()

     # Click on "Hoodies & Sweatshirts" under Category
     hoodies_link = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Hoodies & Sweatshirts')]"))
     )
     self.scroll_into_view(hoodies_link)
     hoodies_link.click()


if __name__ == "__main__":
 suite = unittest.TestSuite()
 suite.addTest(MagentoTest("test_01_navigate_to_product_page"))

 runner = unittest.TextTestRunner(verbosity=2)
 runner.run(suite)