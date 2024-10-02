from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://sbis.ru/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Не найден элемент через локатор {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не найдены элементы через локатор {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def check_title(self):
        title = self.driver.title
        return title

    def validate_url(self):
        cur_url = self.driver.current_url
        return cur_url
