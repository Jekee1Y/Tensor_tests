from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class TensorLocators:
    LOCATOR_BLOCK_SILA = (By.CLASS_NAME, "tensor_ru-Index__block4-bg")
    LOCATOR_ABOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'tensor_ru-Index__link') and contains(@href, '/about')]")


class TensorHelper(BasePage):

    def verify_block_sila(self):
        block = self.find_element(TensorLocators.LOCATOR_BLOCK_SILA), "Блок 'Сила в людях' не найден!"
        return block

    def about_button(self):
        about_buttons = self.find_element(TensorLocators.LOCATOR_ABOUT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", about_buttons)
        about_buttons.click()
