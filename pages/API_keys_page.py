from pages.base_page import BasePage
from locators.API_keys_locators import ApiKeysLocator
from pages.sign_in_page import SignInPage
from test_data.sign_in_page_data import LINK_SIGN_IN_PAGE


class ApiKeysPage(BasePage):

    def open_api_keys_page(self):
        sign_in_page = SignInPage(self.driver, LINK_SIGN_IN_PAGE)
        sign_in_page.open_page()
        sign_in_page.log_in()
        api_key_tab = self.driver.find_element(*ApiKeysLocator.TAB_API_KEYS)
        api_key_tab.click()

    def check_module_title_create_api_key_is_visible(self):
        module_create_api_key = self.driver.find_element(*ApiKeysLocator.MODULE_API_KEY_CREATE)
        assert module_create_api_key.is_displayed(), "module with title “Create key“ does not visible"

    def open_popup_rename_api_key(self):
        edit_api_key_icon = self.driver.find_element(*ApiKeysLocator.EDIT_API_KEY_ICON)
        edit_api_key_icon.click()
        self.driver.switch_to.default_content()

    def enter_new_api_name(self, new_api_name):
        api_key_field = self.element_is_clickable(ApiKeysLocator.API_KEY_FIELD, 10)
        api_key_field.click()
        api_key_field.clear()
        api_key_field.send_keys(new_api_name)

    def click_save_new_api_key_name_button(self):
        save_api_key_name_button = self.driver.find_element(*ApiKeysLocator.SAVE_NEW_API_NAME_BUTTON)
        save_api_key_name_button.click()

    def api_key_name_of_first_row(self):
        return self.driver.find_element(*ApiKeysLocator.API_KEY_NAME_FIRST_ROW).text

    def check_limit_of_api_key_name(self):
        api_name_limit = 20
        actual_length_of_api_key_name = len(self.api_key_name_of_first_row())
        assert actual_length_of_api_key_name == api_name_limit, "The limit of API key name does not correspond to " \
                                                                "expected limit"

    def enter_created_api_key_name(self, new_api_name):
        new_api_key_name_field = self.driver.find_element(*ApiKeysLocator.NEW_API_KEY_NAME)
        new_api_key_name_field.send_keys(new_api_name)

    def check_limit_of_created_api_key_name(self):
        expected_api_name_limit = 20
        created_api_key_name = self.driver.find_element(*ApiKeysLocator.NEW_API_KEY_NAME)
        actual_api_name_limit = int(created_api_key_name.get_attribute('maxlength'))
        assert actual_api_name_limit == expected_api_name_limit, "The limit of created API key name does not correspond to " \
                                                                 "requirements"

    def check_create_api_key_field_is_required(self):
        new_api_key_name_field = self.driver.find_element(*ApiKeysLocator.NEW_API_KEY_NAME)
        is_required = new_api_key_name_field.get_attribute('required')
        assert is_required, "The field hasn't required attribute"

    def check_is_generate_button_clickable(self):
        is_generate_button_clickable = self.element_is_clickable(ApiKeysLocator.GENERATE_BUTTON)
        assert is_generate_button_clickable, "The button does not clickable"

    def click_generate_api_key_name_button(self):
        generate_api_key_button = self.driver.find_element(*ApiKeysLocator.GENERATE_BUTTON)
        generate_api_key_button.click()

    def get_length_of_table_api_keys(self):
        initial_table_api_keys = self.elements_are_visible(ApiKeysLocator.TABLE_API_KEYS_CONTENT)
        return len(initial_table_api_keys)

    def check_is_api_key_generated(self, initial_table_length):
        actual_api_keys_table_length = self.get_length_of_table_api_keys()
        assert actual_api_keys_table_length == initial_table_length + 1, "The new API key does not generated"

    def check_is_success_generate_notice_displayed(self):
        expected_new_api_key_notice_text = 'API key was created successfully'
        actual_new_api_key_notice_text = self.driver.find_element(*ApiKeysLocator.NOTICE_MESSAGE).text
        assert actual_new_api_key_notice_text == expected_new_api_key_notice_text, \
            "The success generate API key notice text does not displayed"

    def get_last_row_elements_from_api_keys_able(self):
        len_t = self.get_length_of_table_api_keys()
        column_values = self.elements_are_visible(ApiKeysLocator.row_elements(self, len_t))
        return column_values

    def check_default_status_generated_api_key(self):
        last_row_elements = self.get_last_row_elements_from_api_keys_able()
        new_generated_api_key_status = last_row_elements[2].text
        assert new_generated_api_key_status == "Active", "The default status of the new API key does not  'Active'"

    def check_is_api_key_tab_active(self):
        api_key_tab_elements = self.driver.find_elements(*ApiKeysLocator.API_KEY_TAB_ELEMENTS)
        initial_view_api_key_tab = api_key_tab_elements[2].get_attribute('class')
        assert initial_view_api_key_tab == "active", "API Keys tab view is not active"

    def check_is_alert_info_displayed(self):
        alert_info_displayed = self.element_is_displayed(ApiKeysLocator.ALERT_INFO)
        assert alert_info_displayed, "Alert info does not displayed"

    def check_module_create_api_key_displayed(self):
        module_create_api_key = self.element_is_displayed(ApiKeysLocator.MODULE_API_KEY_CREATE)
        assert module_create_api_key, "The module 'Create API key' does not displayed"

    def check_is_displayed_api_keys_list(self):
        api_keys_list = self.element_is_displayed(ApiKeysLocator.TABLE_API_KEYS)
        assert api_keys_list, "The API keys list does not displayed"

    def check_is_api_keys_status_displayed(self):
        length_api_keys_table = self.get_length_of_table_api_keys()
        for i in range(1, length_api_keys_table + 1):
            status_display = self.element_is_displayed(ApiKeysLocator.status_api_key(self, i))
            assert status_display, f"The API key status does not display in the row {i}. "
