from .main_page import MainPage
from tests.Folder_groups.test_group_no_pain_no_gain.locators.guide_page_locators import GuidePageLocators as GPL
from .. import links


class GuidePage(MainPage):

    def check_logo(self):
        self.driver.find_element(*GPL.LOGO_LOCATOR).click()
        assert self.driver.current_url == links.HOME_PAGE
