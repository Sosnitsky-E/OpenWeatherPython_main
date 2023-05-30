import pytest
from tests.Folder_groups.test_group_bugs_in_each_step.test_data.urls import *
from tests.Folder_groups.test_group_bugs_in_each_step.pages.main_page import MainPage


@pytest.mark.parametrize('URL', URLs)
def test_tc_003_08_05_about_us_link_is_visible_on_each_page_specified_in_data(driver, URL):
    page = MainPage(driver, link=URL)
    page.open_page()
    page.check_about_us_link_is_visible()

