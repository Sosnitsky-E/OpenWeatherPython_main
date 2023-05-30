from tests.Folder_groups.test_group_100000.pages.api_page import RoadRiskApi


def test_TC_005_08_04_redirection_to_the_how_to_request_road_risk_API_section_of_the_page(driver):
    page = RoadRiskApi(driver)
    page.check_redirect_to_page_section()


def test_TC_005_08_03_road_risk_api_visibility_of_road_risk_api_concept_section(driver):
    page = RoadRiskApi(driver)
    page.check_visibility_concept_section()


def test_TC_005_08_01_road_risk_api_verify_page_title_for_road_risk_api(driver):
    page = RoadRiskApi(driver)
    page.check_module_title_road_risk_page()


def test_TC_005_08_05_redirection_to_the_list_of_sectional_sources_of_weather_warnings_section_of_the_page(driver):
    page = RoadRiskApi(driver)
    page.check_redirection_to_the_section_of_the_page()


def test_TC_005_08_06_verify_redirection_to_the_page_with_API_keys_by_clicking_on_the_API_Key_tab(driver,
                                                                                                  open_and_load_main_page,
                                                                                                  sign_in):
    page = RoadRiskApi(driver)
    page.verify_redirection_to_the_page_with_api_keys()


def test_TC_005_08_07_road_risk_api_verification_of_national_weather_warning_sources_list(driver):
    page = RoadRiskApi(driver)
    page.verification_sources_list()
