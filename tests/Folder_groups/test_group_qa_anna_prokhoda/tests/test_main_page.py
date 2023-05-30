from tests.Folder_groups.test_group_qa_anna_prokhoda.pages.main_page import MainPage


class TestMarketPlaceLinkRedirectsToValidPage:

    def test_TC_002_03_07_marketplace_link_redirects_to_valid_page(self, driver, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.verify_marketplace_link_redirects_to_valid_page()
