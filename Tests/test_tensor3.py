from Pages.SbisMainPage import SbisHelper
from Pages.SbisDownloadPage import SbisDownload


def test_tensor3(browser):
    sbis_main_page = SbisHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.open_local_versions()
    sbis_download_page = SbisDownload(browser)
    sbis_download_page.download_plugin()
    file_path = sbis_download_page.download_wait('F:/download', "sbisplugin-setup-web.exe")
    file_size = sbis_download_page.test_check_file_size(file_path)
    assert abs(file_size - 11.47) < 0.01, f'Ожидаемый размер файла отличается от полученного {file_size}'