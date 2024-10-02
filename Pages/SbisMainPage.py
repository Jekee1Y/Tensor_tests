from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class SbisLocators:
    LOCATOR_SBIS_CONTACTS = (By.XPATH, "//div[contains(@class, 'sbisru-Header-ContactsMenu js-ContactsMenu')]")
    LOCATOR_PANEL_CONTACTS = (By.XPATH, "//div[contains(@class, 'sbisru-Header-ContactsMenu__items-visible')]")
    LOCATOR_MORE_OFFICES = (By.XPATH, "//a[contains(@href, '/contacts')]")
    LOCATOR_LOCAL_VERSIONS = (By.XPATH, "//a[contains(@href, '/download')]")


class SbisHelper(BasePage):

    def open_contacts(self):
        search_field = self.find_element(SbisLocators.LOCATOR_SBIS_CONTACTS)
        search_field.click()
        search_field = self.find_element(SbisLocators.LOCATOR_PANEL_CONTACTS)
        more_offices = self.find_element(SbisLocators.LOCATOR_MORE_OFFICES)
        more_offices.click()

    def open_local_versions(self):
        local_versions = self.find_element(SbisLocators.LOCATOR_LOCAL_VERSIONS)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", local_versions)
        local_versions.click()
