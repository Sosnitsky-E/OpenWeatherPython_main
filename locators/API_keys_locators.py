from selenium.webdriver.common.by import By


class ApiKeysLocator:
    API_KEY_NAME_URL = 'https://home.openweathermap.org/api_keys'
    API_KEY_EDIT_ICON = By.CSS_SELECTOR, "i[class='fa fa-edit']"
    API_KEY_NAME = By.XPATH, "//table/tbody/tr/td[2]"
    API_KEY_ENTER_SELECTOR = By.CSS_SELECTOR, "input[name='edit_key_form[name]']"
    SAVE_BUTTON_SELECTOR = By.CSS_SELECTOR, "button[class='button-round dark']"
    TAB_API_KEYS = By.CSS_SELECTOR, '#myTab [href="/api_keys"]'
    MODULE_API_KEY_CREATE = By.CSS_SELECTOR, '.col-md-4 h4'
    EDIT_API_KEY_ICON = By.CSS_SELECTOR, '.edit_key_btn .fa-edit'
    API_KEY_FIELD = (By.CSS_SELECTOR, '#new_edit_key_form .owm_input')
    SAVE_NEW_API_NAME_BUTTON = By.CSS_SELECTOR, '.pop-up-footer .button-round.dark'
    API_KEY_NAME_FIRST_ROW = By.XPATH, "//div[@class='col-md-8']//tr[1]//td[2]"
    NEW_API_KEY_NAME = By.CSS_SELECTOR, ".new_api_key_form .owm_input"
    GENERATE_BUTTON = By.CSS_SELECTOR, '.new_api_key_form .button-round.dark'
    TABLE_API_KEYS_CONTENT = By.CSS_SELECTOR, "tbody tr"
    NOTICE_MESSAGE = By.XPATH, "//div[@class='panel-body']"
    API_KEY_TAB_ELEMENTS = By.CSS_SELECTOR, '#myTab li'
    ALERT_INFO = By.CSS_SELECTOR, ".alert-info"
    TABLE_API_KEYS = By.CSS_SELECTOR, ".material_table.api-keys"
    SWITCH_STATUS_TO_ACTIVE = By.CSS_SELECTOR, '.fa.fa-toggle-off'
    SWITCH_STATUS_TO_INACTIVE = By.CSS_SELECTOR, '.fa.fa-toggle-on'
    STATUS_COLOR = By.CSS_SELECTOR, "span:nth-child(1)"
    CHANGE_API_KEY_STATUS_ICON = By.XPATH, "//a[@data-method='put']"
    NOTICE_STATUS_API_KEY_CHANGED = By.CSS_SELECTOR, '.panel-body'
    MODAL_WINDOW_EDIT_API_KEY_NAME = By.CSS_SELECTOR, "div[class='pop-up-header'] h3"
    CANCEL_NEW_API_NAME_BUTTON = By.CSS_SELECTOR, '.pop-up-footer .transparent'
    CLOSE_POPUP_NEW_API_KEY_NAME_ICON = By.CSS_SELECTOR, "a[data-dismiss='modal']"
    DELETE_API_KEY_ICON = By.CSS_SELECTOR, '.fa.fa-remove'



    def row_elements(self, row_number):
        t_r = By.XPATH, f"//tbody/tr[{row_number}]/td"
        return t_r

    def status_api_key(self, row_num):
        return By.XPATH, f"//div//tr[{row_num}]/td[3]/span"

