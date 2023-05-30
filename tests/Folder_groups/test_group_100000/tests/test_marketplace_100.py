import pytest
from tests.Folder_groups.test_group_100000.pages.marketplace_page import *
from tests.Folder_groups.test_group_100000.locators.marketplace_page_locators import MarketplaceLocators as M


@pytest.mark.parametrize('locator', [M.STATE_TEXAS])
def test_RF_TC_007_01_01_Select_state_from_dropdown_list(driver, locator):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    page.select_state_field()
    page.select_element_from_dropdown_list(locator)

    expected_state = "Texas"
    selected_state = driver.find_element(*M.STATE_TEXAS).text
    assert expected_state == selected_state, '\n======== WRONG STATE! ========\n'


@pytest.mark.parametrize('locator', [M.YEAR_2019])
def test_RF_TC_007_01_02_Select_year_from_dropdown_list(driver, locator):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    page.select_year_field()
    page.select_element_from_dropdown_list(locator)

    expected_year = "2019"
    selected_year = driver.find_element(*M.EXPECTED_YEAR).text
    assert expected_year == selected_year, '\n======== WRONG YEAR! ========\n'


@pytest.mark.parametrize('locator', [M.WEATHER_PAR_LIST])
def test_RF_TC_007_01_03_Verify_Weather_parameters_to_be_provided(driver, locator):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    elements = page.elements_are_present(locator)
    actual_list = [element.text for element in elements]

    expected_list = ['Temperature', 'Min temperature', 'Max temperature',
                     'Feels like', 'Wind (speed, direction)', 'Pressure',
                     'Humidity', 'Clouds', 'Weather conditions', 'Rain', 'Snow']
    assert expected_list == actual_list, '\n======== WRONG WEATHER PARAMETERS! ========\n'


@pytest.mark.parametrize('locator', [M.UNITS_INFO])
def test_RF_TC_007_01_04_Verify_Units_of_measurement(driver, locator):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    units = page.element_is_present(locator)
    actual_units = units.text

    expected = 'Standard (Kelvin, hPa, meter/sec, mm/h)'
    assert expected == actual_units, '\n======== WRONG UNITS! ========\n'


@pytest.mark.parametrize('locator', [M.FILE_FORMAT_INFO])
def test_RF_TC_007_01_05_Verify_info_about_file_format(driver, locator):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    units = page.element_is_present(locator)
    actual_units = units.text

    expected = 'CSV'
    assert expected == actual_units, '\n======== WRONG FILE FORMAT! ========\n'


def test_RF_TC_007_01_06_Verify_amount_of_order(driver):
    page = MarketplacePage(driver, link=M.URL_HISTORICAL_WEATHER)
    page.open_page()
    page.select_state_field()
    expected_amount = page.find_price_in_dropdown_menu(M.STATE_TEXAS_SUB)
    page.select_element_from_dropdown_list(M.STATE_TEXAS)
    actual_amount = page.find_total_amount(M.TOTAL_AMOUNT)
    assert expected_amount == actual_amount, '\n======== WRONG TOTAL AMOUNT! ========\n'
