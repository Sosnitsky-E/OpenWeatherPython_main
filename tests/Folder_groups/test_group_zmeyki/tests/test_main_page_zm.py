from tests.Folder_groups.test_group_zmeyki.pages.main_page import MainPage


def test_tc_001_08_01_graphic_hourly_forecast_is_displayed(driver, open_and_load_main_page, wait):
    page = MainPage(driver)
    page.graphic_hourly_forecast_is_displayed(wait=wait)


