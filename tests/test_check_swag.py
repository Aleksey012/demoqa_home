from pages.swag_labs import SwagLabs


def test_icon_exist(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.get_url()
    assert swag.exist_icon()




