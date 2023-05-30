from tests.Folder_groups.test_group_zmeyki.locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def graphic_hourly_forecast_is_displayed(self, wait):
        graphic_hourly_forecast = self.driver.find_element(*self.locators.graphic_hourly_forecast_locator)
        self.go_to_element(graphic_hourly_forecast)
        assert self.element_is_visible

