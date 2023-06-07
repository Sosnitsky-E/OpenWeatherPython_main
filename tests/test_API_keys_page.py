

from pages.API_keys_page import ApiKeysPage


class TestApiKey:

    def test_tc_017_01_01_tab_api_keys_is_active(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_api_key_tab_active()

    def test_tc_017_01_02_alert_info_is_displayed_after_oening_api_keys_page(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_alert_info_displayed()

    def test_tc_017_01_03_create_api_key_module_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_module_create_api_key_displayed()

    def test_tc_017_01_04_api_keys_list_is_display(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_displayed_api_keys_list()

    def test_tc_017_02_01_api_keys_status_are_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_api_keys_status_displayed()

    def test_tc_017_04_01_module_title_create_api_key_is_visible(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_module_title_create_api_key_is_visible()

    def test_tc_017_04_02_api_key_name_has_limit_20_characters(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_limit_of_created_api_key_name()

    def test_tc_017_04_03_api_key_name_is_required(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_create_api_key_field_is_required()

    def test_tc_017_04_04_api_key_generate_button_is_clickable(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_generate_button_clickable()

    def test_tc_017_04_05_api_key_is_generated(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name("Generate name")
        initial_api_keys_table_length = api_keys_page.get_length_of_table_api_keys()
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.check_is_api_key_generated(initial_api_keys_table_length)

    def test_tc_017_04_06_generate_successfully_notice_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name("Generate name 1")
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.check_is_success_generate_notice_displayed()

    def test_tc_017_04_06_new_api_key_default_status_is_active(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name("Default status check name ")
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.check_default_status_generated_api_key()
