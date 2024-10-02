from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By


class TensorAboutLocators:
    LOCATOR_CONTAINER_WITH_IMG = (By.XPATH, "//div[contains(@class, 'tensor_ru-section tensor_ru-About__block3')]")


class TensorAbout(BasePage):

    def check_images_size(self):
        container_images = self.find_element(TensorAboutLocators.LOCATOR_CONTAINER_WITH_IMG)
        image = container_images.find_elements(By.TAG_NAME, 'img')
        sizes = [img.size for img in image]
        return image, sizes