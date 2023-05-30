from tests.Folder_groups.test_group_no_pain_no_gain.pages.partners_page import Partners
from tests.Folder_groups.test_group_no_pain_no_gain import links
from tests.Folder_groups.test_group_no_pain_no_gain.test_data.partners_page_data import PartnersPageData as PPD
from tests.Folder_groups.test_group_no_pain_no_gain.locators.partners_page_locators import PartnersPageLocators as PPL

class TestPartnersPage:
    def test_TC_011_01_01_verify_that_Partners_and_solutions_page_title_is_correct(self, driver):
        page = Partners(driver, link=links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.check_page_title(PPD.PARTNERS_PAGE_TITLE)

    def test_TC_011_20_01_verify_that_the_info_board_message_at_the_top_of_the_page_is_displayed(self, driver):
        page = Partners(driver, links.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.get_text_content_of_the_element(PPL.PARTENERS_PAGE_INFO_BOARD, PPD.PARTENERS_PAGE_INFO_BOARD_TEXT)
