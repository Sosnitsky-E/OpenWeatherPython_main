from tests.Folder_groups.test_group_no_pain_no_gain.pages.footer import Footer
from tests.Folder_groups.test_group_no_pain_no_gain import links
from tests.Folder_groups.test_group_no_pain_no_gain.locators.footer_locators import FooterLocators as FL

class TestFooter:
    def test_TC_003_08_02_ask_a_question_link_is_visible(self, driver, open_and_load_main_page):
        page = Footer(driver)
        page.element_visibility(FL.ASK_A_QUESTION_LINK)

    def test_TC_003_08_03_ask_a_question_link_is_clickable(self, driver, open_and_load_main_page):
        page = Footer(driver)
        page.element_clickability(FL.ASK_A_QUESTION_LINK)

    def test_TC_003_12_05_ask_a_question_link_leads_to_correct_page(self, driver, open_and_load_main_page):
        page = Footer(driver)
        page.scroll_down_the_page()
        page.check_link_in_new_window(FL.ASK_A_QUESTION_LINK, links.ASK_A_QUESTION_PAGE)

    def test_TC_003_08_07_blog_link_is_visible(self, driver, open_and_load_main_page):
        page = Footer(driver)
        page.element_visibility(FL.BLOG_LINK)

    def test_TC_003_08_08_blog_link_is_clickable(self, driver, open_and_load_main_page):
        page = Footer(driver)
        page.element_clickability(FL.BLOG_LINK)

    def test_TC_003_13_02_clickability_of_Manage_cookies_button(self, driver, open_and_load_main_page):
        page = Footer(driver)
        page.element_clickability(FL.MANAGE_COOKIES)
