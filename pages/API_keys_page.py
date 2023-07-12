import time

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

    def open_popup_rename_api_key(self):
        edit_api_key_icon = self.driver.find_element(*ApiKeysLocator.EDIT_API_KEY_ICON)
        edit_api_key_icon.click()
        self.driver.switch_to.default_content()

    def clear_new_api_key_name_field(self):
        self.clear_the_field(ApiKeysLocator.API_KEY_FIELD)

    def enter_new_api_key_name(self, new_api_name):
        api_key_field = self.clear_the_field(ApiKeysLocator.API_KEY_FIELD)
        api_key_field.send_keys(new_api_name)

    def click_save_new_api_key_name_button(self):
        save_api_key_name_button = self.driver.find_element(*ApiKeysLocator.SAVE_NEW_API_NAME_BUTTON)
        save_api_key_name_button.click()

    def click_cancel_new_api_key_name_button(self):
        cancel_button = self.element_is_clickable(ApiKeysLocator.CANCEL_NEW_API_NAME_BUTTON)
        cancel_button.click()

    def click_close_icon_of_new_api_key_name_popup(self):
        cancel_button = self.element_is_clickable(ApiKeysLocator.CLOSE_POPUP_NEW_API_KEY_NAME_ICON)
        cancel_button.click()

    def api_key_name_of_first_row(self):
        return self.driver.find_element(*ApiKeysLocator.API_KEY_NAME_FIRST_ROW).text

    def enter_created_api_key_name(self, new_api_name):
        new_api_key_name_field = self.driver.find_element(*ApiKeysLocator.NEW_API_KEY_NAME)
        new_api_key_name_field.send_keys(new_api_name)

    def click_generate_api_key_name_button(self):
        generate_api_key_button = self.driver.find_element(*ApiKeysLocator.GENERATE_BUTTON)
        generate_api_key_button.click()

    def click_delete_api_key_icon(self):
        delete_icon = self.driver.find_element(*ApiKeysLocator.DELETE_API_KEY_ICON)
        delete_icon.click()

    def get_length_of_table_api_keys(self):
        initial_table_api_keys = self.elements_are_visible(ApiKeysLocator.TABLE_API_KEYS_CONTENT)
        return len(initial_table_api_keys)

    def get_last_row_elements_from_api_keys_table(self):
        len_t = self.get_length_of_table_api_keys()
        column_values = self.elements_are_visible(ApiKeysLocator.row_elements(self, len_t))
        return column_values

    def get_row_elements_by_number_from_api_keys_table(self, row_num):
        column_values = self.elements_are_visible(ApiKeysLocator.row_elements(self, row_num))
        return column_values

    def get_api_key_initial_status(self, row_num):
        row_values = self.get_row_elements_by_number_from_api_keys_table(row_num)
        initial_status_api_key = row_values[2].text
        return initial_status_api_key

    def click_switch_status_icon(self, row_num):
        first_column_values = self.get_row_elements_by_number_from_api_keys_table(row_num)
        initial_status = self.get_api_key_initial_status(row_num)
        if initial_status == "Inactive":
            switch_status = first_column_values[3].find_element(*ApiKeysLocator.SWITCH_STATUS_TO_ACTIVE)
            switch_status.click()
            alert = self.driver.switch_to.alert
            alert.accept()
        else:
            switch_status = first_column_values[3].find_element(*ApiKeysLocator.SWITCH_STATUS_TO_INACTIVE)
            switch_status.click()
            alert = self.driver.switch_to.alert
            alert.accept()

    def delete_api_key(self):
        self.click_delete_api_key_icon()
        alert = self.driver.switch_to.alert
        alert.accept()

    def leave_one_row_in_the_table(self):
        row_numbers = self.get_length_of_table_api_keys()
        while row_numbers > 1:
            self.delete_api_key()
            row_numbers -= 1

    def add_row_in_table(self):
        rows = self.get_length_of_table_api_keys()
        if rows == 1:
            self.enter_created_api_key_name("New row in table")
            self.click_generate_api_key_name_button()

    def check_module_title_create_api_key_is_visible(self):
        module_create_api_key = self.driver.find_element(*ApiKeysLocator.MODULE_API_KEY_CREATE)
        assert module_create_api_key.is_displayed(), "module with title “Create key“ is not visible"

    def check_limit_of_api_key_name_field(self):
        api_key_name_field_limit = 20
        api_key_name_field = self.driver.find_element(*ApiKeysLocator.API_KEY_FIELD)
        actual_length_of_api_key_name_field = int(api_key_name_field.get_attribute('maxlength'))
        assert actual_length_of_api_key_name_field == api_key_name_field_limit, "The limit of API key name" \
                                                                                " field  is not correspond to " \
                                                                                "expected limit."

    def check_limit_of_created_api_key_name(self):
        expected_api_name_limit = 20
        created_api_key_name = self.driver.find_element(*ApiKeysLocator.NEW_API_KEY_NAME)
        actual_api_name_limit = int(created_api_key_name.get_attribute('maxlength'))
        assert actual_api_name_limit == expected_api_name_limit, "The limit of created API key name" \
                                                                 " is not correspond to requirements"

    def check_create_api_key_field_is_required(self):
        new_api_key_name_field = self.driver.find_element(*ApiKeysLocator.NEW_API_KEY_NAME)
        is_required = new_api_key_name_field.get_attribute('required')
        assert is_required, "The field hasn't required attribute"

    def check_is_generate_button_clickable(self):
        is_generate_button_clickable = self.element_is_clickable(ApiKeysLocator.GENERATE_BUTTON)
        assert is_generate_button_clickable, "The button is not clickable"

    def check_is_api_key_generated(self, initial_table_length):
        actual_api_keys_table_length = self.get_length_of_table_api_keys()
        assert actual_api_keys_table_length == initial_table_length + 1, "The new API key is not generated"

    def check_is_success_generate_notice_displayed(self):
        expected_new_api_key_notice_text = 'API key was created successfully'
        actual_new_api_key_notice_text = self.driver.find_element(*ApiKeysLocator.NOTICE_MESSAGE).text
        assert actual_new_api_key_notice_text == expected_new_api_key_notice_text, \
            "The success generate API key notice text is not displayed"

    def check_default_status_generated_api_key(self):
        last_row_elements = self.get_last_row_elements_from_api_keys_table()
        new_generated_api_key_status = last_row_elements[2].text
        assert new_generated_api_key_status == "Active", "The default status of the new API key is not  'Active'"

    def check_is_api_key_tab_active(self):
        api_key_tab_elements = self.driver.find_elements(*ApiKeysLocator.API_KEY_TAB_ELEMENTS)
        initial_view_api_key_tab = api_key_tab_elements[2].get_attribute('class')
        assert initial_view_api_key_tab == "active", "API Keys tab view is not active"

    def check_is_main_alert_info_displayed(self):
        alert_info_displayed = self.element_is_displayed(ApiKeysLocator.ALERT_INFO)
        assert alert_info_displayed, "Alert info is not displayed"

    def check_module_create_api_key_displayed(self):
        module_create_api_key = self.element_is_displayed(ApiKeysLocator.MODULE_API_KEY_CREATE)
        assert module_create_api_key, "The module 'Create API key' is not displayed"

    def check_is_displayed_api_keys_list(self):
        api_keys_list = self.element_is_displayed(ApiKeysLocator.TABLE_API_KEYS)
        assert api_keys_list, "The API keys list is not displayed"

    def check_is_api_keys_status_displayed(self):
        length_api_keys_table = self.get_length_of_table_api_keys()
        for i in range(1, length_api_keys_table + 1):
            status_display = self.element_is_displayed(ApiKeysLocator.status_api_key(self, i))
            assert status_display, f"The API key status does not display in the row {i}. "

    def check_is_status_api_key_changed(self, initial_status_api_key, row_num):
        current_status = self.get_api_key_initial_status(row_num)
        assert current_status != initial_status_api_key, "API Key status has not changed"

    def check_is_status_api_key_red(self, row_num):
        row_values = self.get_row_elements_by_number_from_api_keys_table(row_num)
        color = row_values[2].find_element(*ApiKeysLocator.STATUS_COLOR).value_of_css_property("color")
        assert "255, 0, 0," in color, "The inactive API key status is not red"

    def check_is_status_api_key_black(self, row_num):
        row_values = self.get_row_elements_by_number_from_api_keys_table(row_num)
        color = row_values[2].find_element(*ApiKeysLocator.STATUS_COLOR).value_of_css_property("color")
        assert "72, 72, 74" in color, "The inactive API key status is not black"

    def check_is_icon_change_api_key_status_displayed(self):
        change_status_icons = self.elements_are_visible(ApiKeysLocator.CHANGE_API_KEY_STATUS_ICON)
        assert change_status_icons, "One of the change API key status icon is not display in the table"

    def check_is_icon_deactivate_api_key_displayed(self):
        length_api_keys_table = self.get_length_of_table_api_keys()
        for i in range(1, length_api_keys_table + 1):
            initial_status = self.get_api_key_initial_status(i)
            if initial_status == "Inactive":
                self.click_switch_status_icon(i)
            deactivate_api_key_displayed = self.element_is_displayed(ApiKeysLocator.SWITCH_STATUS_TO_INACTIVE)
            assert deactivate_api_key_displayed, "The icon Deactivate API key is not displayed"

    def check_is_icon_activate_api_key_displayed(self):
        length_api_keys_table = self.get_length_of_table_api_keys()
        for i in range(1, length_api_keys_table + 1):
            initial_status = self.get_api_key_initial_status(i)
            if initial_status == "Active":
                self.click_switch_status_icon(i)
            deactivate_api_key_displayed = self.element_is_displayed(ApiKeysLocator.SWITCH_STATUS_TO_ACTIVE)
            assert deactivate_api_key_displayed, "The icon Deactivate API key is not displayed"

    def check_change_api_key_status_icon_is_clickable(self):
        change_api_key_status_icon_clickable = self.element_is_clickable(ApiKeysLocator.CHANGE_API_KEY_STATUS_ICON)
        assert change_api_key_status_icon_clickable, "The icon for changing API key status is not clickable"

    def check_alert_for_confirming_change_api_key_status_is_displayed(self):
        expected_alert_text1 = 'Do you want to deactivate this key?'
        expected_alert_text2 = "Do you want to activate this key?"
        change_api_key_status_icon = self.element_is_clickable(ApiKeysLocator.CHANGE_API_KEY_STATUS_ICON)
        change_api_key_status_icon.click()
        alert = self.driver.switch_to.alert
        actual_alert_text = alert.text
        assert actual_alert_text == expected_alert_text1 or expected_alert_text2, \
            "The alert text is not correspond to expected"

    def check_is_notice_API_key_status_changed_is_displayed(self):
        expected_notice1 = 'API key was activated successfully'
        expected_notice2 = "API key was deactivated successfully"
        change_api_key_status_icon = self.element_is_clickable(ApiKeysLocator.CHANGE_API_KEY_STATUS_ICON)
        change_api_key_status_icon.click()
        alert = self.driver.switch_to.alert
        alert.accept()
        actual_notice_api_key_statis_changed = self.element_is_visible(ApiKeysLocator.NOTICE_STATUS_API_KEY_CHANGED) \
            .text
        assert actual_notice_api_key_statis_changed == expected_notice2 or expected_notice1, "Incorrect text for the" \
                                                                                             " Change API Key status" \
                                                                                             " notice"

    def check_the_api_key_status_does_not_changed(self):
        initial_status = self.get_api_key_initial_status(1)
        change_api_key_status_icon = self.element_is_clickable(ApiKeysLocator.CHANGE_API_KEY_STATUS_ICON)
        change_api_key_status_icon.click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        actual_api_status = self.get_api_key_initial_status(1)
        assert actual_api_status == initial_status, "API status was changed after click Cancel button"

    def check_if_api_key_name_displayed(self):
        api_key_name_displayed = self.element_is_displayed(ApiKeysLocator.API_KEY_NAME)
        assert api_key_name_displayed, "API key name is not displayed"

    def check_if_edit_api_key_icon_is_displayed(self):
        edit_api_key_icon = self.element_is_displayed(ApiKeysLocator.EDIT_API_KEY_ICON)
        assert edit_api_key_icon, "The icon for editing API key name is not displayed."

    def check_is_displayed_modal_window_for_change_api_key_name(self):
        modal_window_for_change_api_key_name = self.element_is_visible(ApiKeysLocator.MODAL_WINDOW_EDIT_API_KEY_NAME,
                                                                       10)
        assert modal_window_for_change_api_key_name.text == "Edit API key name", \
            "The modal window Edit API key name is not displayed"

    def check_is_displayed_field_api_key_name(self):
        assert self.element_is_displayed(ApiKeysLocator.API_KEY_FIELD), "The field 'API key name' is not display"

    def check_is_saved_new_api_key_name(self, api_key_name):
        new_api_key_name = self.api_key_name_of_first_row()
        assert new_api_key_name == api_key_name, "The entered API key name is not saved."

    def check_if_api_key_name_is_not_changed_clicking_cancel_button(self, api_key_name):
        expected_api_key_name = self.api_key_name_of_first_row()
        assert expected_api_key_name == api_key_name, "The API key name changes after clicking the 'Cancel' button."

    def check_if_api_key_name_is_not_changed_clicking_close_icon(self, api_key_name):
        expected_api_key_name = self.api_key_name_of_first_row()
        assert expected_api_key_name == api_key_name, "The API key name changes after clicking the 'Close' icon."

    def check_api_key_name_remains_unchanged_if_new_name_is_not_entered(self, api_key_name):
        expected_api_key_name = self.api_key_name_of_first_row()
        assert expected_api_key_name == api_key_name, " API key name is changed when the user clears the " \
                                                      "New API key name field and clicks the Save button."

    def check_api_key_name_remains_unchanged_when_new_name_entered_as_spaces(self, api_key_name):
        expected_api_key_name = self.api_key_name_of_first_row()
        assert expected_api_key_name == api_key_name, " API key name is changed when the user enter spaces."

    def check_is_notice_new_API_key_name_saved_is_displayed(self):
        expected_notice = 'API key was edited successfully'
        actual_notice = self.driver.find_element(*ApiKeysLocator.NOTICE_MESSAGE).text
        assert actual_notice == expected_notice, "The notice indicating the successful editing of" \
                                                 " the API key name is not displayed"

    def check_delete_api_key_button_is_displayed(self):
        assert self.element_is_displayed(ApiKeysLocator.DELETE_API_KEY_ICON), "The icon delete API key is not" \
                                                                              " displayed."

    def check_that_api_key_rows_number_more_one(self):
        rows_number = self.get_length_of_table_api_keys()
        assert rows_number > 1, "The table API keys contains only one row."

    def check_delete_popup_is_displayed(self):
        assert self.alert_is_displayed(), "The popup for the approval of deleting the selected API key is not displayed"

    def check_text_in_the_popup_delete_api_key(self):
        expected_text = "Do you want to remove this key?"
        alert = self.driver.switch_to.alert
        actual_text = alert.text
        assert actual_text == expected_text, "The clarifying question is not displayed in the popup" \
                                             " to remove the API key."

    def check_delete_api_key_button_is_not_displayed(self):
        delete_icon = self.element_is_displayed(ApiKeysLocator.DELETE_API_KEY_ICON)
        assert not delete_icon, "The icon delete API key is displayed."

    def check_api_key_is_not_deleted(self, rows):
        initial_row_number = rows
        alert = self.driver.switch_to.alert
        alert.dismiss()
        actual_row_number = self.get_length_of_table_api_keys()
        assert actual_row_number == initial_row_number, "The API key is deleted."
