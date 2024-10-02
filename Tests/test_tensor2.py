from Pages.SbisMainPage import SbisHelper
from Pages.SbisContactPage import SbisContactHelper


def test_sbis2(browser):
    sbis_main_page = SbisHelper(browser)
    sbis_main_page.go_to_site()
    sbis_main_page.open_contacts()
    sbis_contact_page = SbisContactHelper(browser)
    region = sbis_contact_page.check_region()
    assert region == 'Ивановская обл.', "Регион не совпадает"
    block_partners = sbis_contact_page.check_partners()
    assert block_partners, "Блок партнеров не найден"
    sbis_contact_page.change_region()
    new_region = sbis_contact_page.check_region()
    assert new_region == 'Камчатский край', "Новый регион не совпадает"
    new_partner_region = sbis_contact_page.check_region_partners()
    assert new_partner_region == 'Петропавловск-Камчатский', "Регион партнеров не изменился"
    title = sbis_contact_page.check_title()
    assert 'Камчатский край' in title, 'Заголовки не совпадают'
    new_url = sbis_contact_page.validate_url()
    assert '41-kamchatskij-kraj' in new_url, "URL не совпадает"
