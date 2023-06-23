from pages.API_keys_page import ApiKeysPage


class TestApiKey:

    def test_tc_017_01_01_tab_api_keys_is_active(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_api_key_tab_active()

    def test_tc_017_01_02_alert_info_is_displayed_after_opening_api_keys_page(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_main_alert_info_displayed()

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

    def test_tc_017_02_02_the_status_of_api_key_is_changed(self, driver):
        row_num = 1
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_status = api_keys_page.get_api_key_initial_status(row_num)
        api_keys_page.click_switch_status_icon(row_num)
        api_keys_page.check_is_status_api_key_changed(initial_status, row_num)

    def test_tc_017_02_03_the_inactive_status_of_api_key_is_red(self, driver):
        row_num = 1
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_status = api_keys_page.get_api_key_initial_status(row_num)
        if initial_status == "Active":
            api_keys_page.click_switch_status_icon(row_num)
        api_keys_page.check_is_status_api_key_red(row_num)

    def test_tc_017_02_04_icon_change_status_api_key_is_display(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_icon_change_api_key_status_displayed()

    def test_tc_017_02_05_the_icon_deactivate_api_key_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_icon_deactivate_api_key_displayed()

    def test_tc_017_02_06_the_icon_change_api_key_status_is_clickable(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_change_api_key_status_icon_is_clickable()

    def test_tc_017_02_07_notice_API_key_status_change_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_notice_API_key_status_change_is_displayed()

    def test_tc_017_02_08_the_active_status_of_api_key_is_black(self, driver):
        row_num = 1
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_status = api_keys_page.get_api_key_initial_status(row_num)
        if initial_status == "Inactive":
            api_keys_page.click_switch_status_icon(row_num)
        api_keys_page.check_is_status_api_key_black(row_num)

    def test_tc_017_02_09_the_icon_activate_api_key_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_icon_activate_api_key_displayed()

    def test_tc_017_02_10_the_alert_for_changing_api_key_status_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_alert_for_confirming_change_api_key_status_is_displayed()

    def test_tc_017_02_11_the_api_key_status_does_not_changed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_the_api_key_status_does_not_changed()

    def test_tc_017_03_01_the_api_key_name_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_if_api_key_name_displayed()

    def test_tc_017_03_02_the_new_api_key_name_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.open_popup_rename_api_key()
        api_keys_page.enter_new_api_name("Changed API key name")
        api_keys_page.click_save_new_api_key_name_button()
        api_keys_page.check_if_api_key_name_displayed()

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
