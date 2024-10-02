from Pages.SbisMainPage import SbisHelper
from Pages.TensorPage import TensorHelper
from Pages.SbisContactPage import SbisContactHelper
from Pages.TensorAbourPage import TensorAbout


def test_sbis1(browser):
    sbis_main_page = SbisHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.open_contacts()
    sbis_contact_page = SbisContactHelper(browser)
    sbis_contact_page.tensor_banner()
    browser.switch_to.window(browser.window_handles[-1])
    tensor_url = sbis_contact_page.validate_url()
    assert tensor_url == 'https://tensor.ru/', f'Страница {tensor_url} не совпадает с ожидаемой'

    tensor_page = TensorHelper(browser)
    block_sila = tensor_page.verify_block_sila()
    assert block_sila, "Блок не найдет"
    tensor_page.about_button()
    tensor_about_url = tensor_page.validate_url()
    assert tensor_about_url == 'https://tensor.ru/about', f'Страница {tensor_about_url} не совпадает с ожидаемой'
    tensor_about_page = TensorAbout(browser)
    images, sizes = tensor_about_page.check_images_size()
    assert images, "Изображения не найдены"
    assert all(size == sizes[0] for size in sizes), "Не все изображения имеют одинаковый размер"