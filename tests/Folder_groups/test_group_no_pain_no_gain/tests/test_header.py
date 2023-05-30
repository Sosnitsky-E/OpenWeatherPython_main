from tests.Folder_groups.test_group_no_pain_no_gain.pages.header import Header
from tests.Folder_groups.test_group_no_pain_no_gain.locators.header_locators import HeaderLocators as HL
from tests.Folder_groups.test_group_no_pain_no_gain.locators.partners_page_locators import PartnersPageLocators as PPL
from tests.Folder_groups.test_group_no_pain_no_gain import links


class TestHeader:

    def test_TC_002_03_22_partners_link_is_visible_and_clickable(self, driver, open_and_load_main_page):
        page = Header(driver)
        page.element_visibility_and_clickability(HL.PARTNERS_LINK, links.PARTNERS_AND_SOLUTIONS)

    def test_partners_link_leads_to_page_with_correct_header(self, driver, open_and_load_main_page):
        page = Header(driver)
        page.link_leads_to_page_with_correct_header(HL.PARTNERS_LINK, PPL.PARTNERS_PAGE_HEADER)
