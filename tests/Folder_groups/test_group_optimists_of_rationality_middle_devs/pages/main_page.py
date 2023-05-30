from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    def sample_function(self):
        return self
