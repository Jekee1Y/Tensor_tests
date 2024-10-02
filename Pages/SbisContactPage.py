from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SbisContactLocators:
    LOCATOR_TENSOR_BANNER = (By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
    LOCATOR_ACTUAL_REGION = (By.XPATH, "//span[contains(@class, 'sbis_ru-Region-Chooser__text')]") 
    LOCATOR_PARTNERS = (By.XPATH, "//div[contains(@class, 'sbisru-Contacts-List__col ws-flex-shrink-1')]")
    LOCATOR_CHANGE_REGION = (By.XPATH, "//span[contains(@class, 'sbis_ru-link') and contains(@title, 'Камчатский край')]")
    LOCATOR_PARTNERS_CITY = (By.ID, "city-id-2")


class SbisContactHelper(BasePage):

    def tensor_banner(self):
        banner_tensor = self.find_element(SbisContactLocators.LOCATOR_TENSOR_BANNER)
        banner_tensor.click()

    def check_region(self):
        region_auto = self.find_element(SbisContactLocators.LOCATOR_ACTUAL_REGION)
        region = region_auto.text
        return region

    def check_partners(self):
        block_partners = self.find_element(SbisContactLocators.LOCATOR_PARTNERS)
        return block_partners

    def change_region(self):
        region_status = self.find_element(SbisContactLocators.LOCATOR_ACTUAL_REGION)
        region_status.click()
        region_status = self.find_element(SbisContactLocators.LOCATOR_CHANGE_REGION)
        region_status.click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(SbisContactLocators.LOCATOR_ACTUAL_REGION, "Камчатский край")
        )

    def check_region_partners(self):
        new_region = self.find_element(SbisContactLocators.LOCATOR_PARTNERS_CITY).text
        return new_region
