from Pages.BaseApp import BasePage
from selenium.webdriver.common.by import By
import os
import time


class SbisDownloadLocators:
    LOCATOR_SBIS_PLUGIN = (By.XPATH, "//div[contains(@class, 'controls-TabButton__caption') and contains(text(), 'СБИС Плагин')]")
    LOCATOR_DOWNLOAD = (By.XPATH, "//a[contains(@href, 'master/win32/sbisplugin-setup-web.exe')]")


class SbisDownload(BasePage):

    def download_plugin(self):
        sbis_plugin = self.find_element(SbisDownloadLocators.LOCATOR_SBIS_PLUGIN)
        sbis_plugin.click()
        sbis_download = self.find_element(SbisDownloadLocators.LOCATOR_DOWNLOAD)
        sbis_download.click()

    def download_wait(self, path_to_downloads, file_name):
        seconds = 0
        dl_wait = True
        while dl_wait and seconds < 10:
            time.sleep(1)
            dl_wait = False
            for fname in os.listdir(path_to_downloads):
                if fname.endswith('.exe'):
                    dl_wait = True
            seconds += 1
        file_path = os.path.join(path_to_downloads, file_name)
        print(file_path)
        return file_path

    def test_check_file_size(self, file_path):
        file_size = os.path.getsize(file_path) / (1024*1024)
        return file_size
