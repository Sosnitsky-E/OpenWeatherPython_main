import allure
from allure_commons.types import AttachmentType

from pages.API_keys_page import ApiKeysPage


class TestApiKey:

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("US_017.01")
    @allure.feature("Open page API key")
    def test_tc_017_01_01_tab_api_keys_is_active(self, driver):
        """
        In this test, we check that when you open the API Keys tab, it is marked as active with an orange underline.
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.get_screenshot_allure("Open API page")
        api_keys_page.check_is_api_key_tab_active()

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("US_017.01")
    @allure.feature("Open page API key")
    def test_tc_017_01_02_alert_info_is_displayed_after_opening_api_keys_page(self, driver):
        """
        In this test case, it is checked that when you open the API Keys tab, a notice message that you have
         the ability to generate the necessary number of keys is displayed.
         """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_main_alert_info_displayed()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("US_017.01")
    @allure.feature("Open page API key")
    def test_tc_017_01_03_create_api_key_module_is_displayed(self, driver):
        """
        In this test case, it is checked that the module for creating a new API key is displayed
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_module_create_api_key_displayed()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("US_017.01")
    @allure.feature("Open page API key")
    def test_tc_017_01_04_api_keys_list_is_display(self, driver):
        """
        In this test case, it is checked that the list of all created API keys is displayed
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_displayed_api_keys_list()

    @allure.severity(allure.severity_level.NORMAL)
    def test_tc_017_02_01_api_keys_status_are_displayed(self, driver):
        """
            In this test case, it is checked that the initial status of API key is displayed
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_api_keys_status_displayed()

    def test_tc_017_02_02_the_status_of_api_key_is_changed(self, driver):
        """
        In this test case, it is checked that the status of the API key changes after clicking the
        'Change API key status' icon.
        """
        row_num = 1
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_status = api_keys_page.get_api_key_initial_status(row_num)
        api_keys_page.click_switch_status_icon(row_num)
        api_keys_page.check_is_status_api_key_changed(initial_status, row_num)

    def test_tc_017_02_03_the_inactive_status_of_api_key_is_red(self, driver):
        """
        In this test case, it is checked that the color of the API key's inactive status is red.
        """
        row_num = 1
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_status = api_keys_page.get_api_key_initial_status(row_num)
        if initial_status == "Active":
            api_keys_page.click_switch_status_icon(row_num)
        api_keys_page.check_is_status_api_key_red(row_num)

    def test_tc_017_02_04_icon_change_status_api_key_is_display(self, driver):
        """
        In this test case, it is checked that the icon 'Change status API key' is displayed.
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_icon_change_api_key_status_displayed()

    def test_tc_017_02_05_the_icon_deactivate_api_key_is_displayed(self, driver):
        """
        In this test case , it is checked that the icon  'Deactivate API key' is displayed.
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_icon_deactivate_api_key_displayed()

    def test_tc_017_02_06_the_icon_change_api_key_status_is_clickable(self, driver):
        """
        In this test case, it is checked that the icon 'Change status API key' is clickable.
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_change_api_key_status_icon_is_clickable()

    def test_tc_017_02_07_notice_API_key_status_change_is_displayed(self, driver):
        """
       In this test case, it is checked that when you change the API Keys status,
        a notice message that the API key status has been changed successfully is displayed.
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_notice_API_key_status_changed_is_displayed()

    def test_tc_017_02_08_the_active_status_of_api_key_is_black(self, driver):
        """
        In this test case, it is checked that the color of the API key's active status is black.
        """
        row_num = 1
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_status = api_keys_page.get_api_key_initial_status(row_num)
        if initial_status == "Inactive":
            api_keys_page.click_switch_status_icon(row_num)
        api_keys_page.check_is_status_api_key_black(row_num)

    def test_tc_017_02_09_the_icon_activate_api_key_is_displayed(self, driver):
        """
        In this test case , it is checked that the icon  'Deactivate API key' is displayed.
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_is_icon_activate_api_key_displayed()

    def test_tc_017_02_10_the_alert_for_changing_api_key_status_is_displayed(self, driver):
        """
        In this test case , it is checked that the alert for confirming the change of API key status is displayed
        after clicking the 'Change API key status' icon.
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_alert_for_confirming_change_api_key_status_is_displayed()

    def test_tc_017_02_11_the_api_key_status_does_not_changed(self, driver):
        """
        In this test case, it is checked that the API key status does not change when clicking the 'Cancel' button
        in the alert.
        """
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
        api_keys_page.enter_new_api_key_name("Changed API key name")
        api_keys_page.click_save_new_api_key_name_button()
        api_keys_page.check_if_api_key_name_displayed()

    def test_tc_017_03_03_the_icon_for_change_api_key_name_is_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.check_if_edit_api_key_icon_is_displayed()

    def test_tc_017_03_04_the_modal_window_edit_api_key_name_displayed(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.open_popup_rename_api_key()
        api_keys_page.check_is_displayed_modal_window_for_change_api_key_name()

    def test_tc_017_03_05_the_field_api_key_name_displayed_in_modal_window(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.open_popup_rename_api_key()
        api_keys_page.check_is_displayed_field_api_key_name()

    def test_tc_017_03_06_the_new_api_key_name_is_saved(self, driver):
        new_api_key_name = "API key name save"
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.open_popup_rename_api_key()
        api_keys_page.enter_new_api_key_name(new_api_key_name)
        api_keys_page.click_save_new_api_key_name_button()
        api_keys_page.check_is_saved_new_api_key_name(new_api_key_name)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("US_017.03")
    @allure.feature("API key name change")
    def test_tc_017_03_07_the_api_key_name_is_not_changed_cancel_button(self, driver):
        """
        In this test case , it is checked that the API key name has not changed after clicking "Cancel" button.
        """
        new_api_key_name = "any API key name "
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_api_key_name = api_keys_page.api_key_name_of_first_row()
        api_keys_page.open_popup_rename_api_key()
        api_keys_page.enter_new_api_key_name(new_api_key_name)
        api_keys_page.click_cancel_new_api_key_name_button()
        api_keys_page.check_if_api_key_name_is_not_changed_clicking_cancel_button(initial_api_key_name)

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("US_017.03")
    @allure.feature("API key name change")
    def test_tc_017_03_08_the_api_key_name_is_not_changed_close_icon(self, driver):
        """
        In this test case , it is checked that the API key name has not changed after clicking popup's "Close" icon.
        """
        new_api_key_name = "any API key name "
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_api_key_name = api_keys_page.api_key_name_of_first_row()
        api_keys_page.open_popup_rename_api_key()
        api_keys_page.enter_new_api_key_name(new_api_key_name)
        api_keys_page.click_close_icon_of_new_api_key_name_popup()
        api_keys_page.check_if_api_key_name_is_not_changed_clicking_close_icon(initial_api_key_name)

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story("US_017.03")
    @allure.feature("API key name change")
    def test_tc_017_03_09_the_api_key_name_is_not_changed_if_field_empty(self, driver):
        """
        In this test case, we are checking whether the API key name remains unchanged when
         the user clears the "New API key name" field and clicks the "Save" button.
        """
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        initial_api_key_name = api_keys_page.api_key_name_of_first_row()
        api_keys_page.open_popup_rename_api_key()
        api_keys_page.clear_new_api_key_name_field()
        api_keys_page.click_save_new_api_key_name_button()
        api_keys_page.check_api_key_name_remains_unchanged_if_new_name_is_not_entered(initial_api_key_name)

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

    def test_tc_017_04_07_new_api_key_default_status_is_active(self, driver):
        api_keys_page = ApiKeysPage(driver)
        api_keys_page.open_api_keys_page()
        api_keys_page.enter_created_api_key_name("Default status check name ")
        api_keys_page.click_generate_api_key_name_button()
        api_keys_page.check_default_status_generated_api_key()
