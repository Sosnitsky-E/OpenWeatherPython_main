from tests.Folder_groups.test_group_trust_me_i_am_engineer.pages.partners_page import PartnersPage


def test_TC_011_03_01_verify_the_link_view_on_github_is_visible(driver):
    page = PartnersPage(driver)
    page.verify_the_link_view_on_github_is_visible()

def test_TC_011_11_01_verify_redirection_of_the_link_to_the_right_website(driver):
    page = PartnersPage(driver)
    page.verify_redirection_drupal_button_leads_to_the_new_website()

def test_TC_011_03_02_verify_the_link_view_on_github_is_clickable(driver):
    page = PartnersPage(driver)
    page.verify_the_link_view_on_github_is_clickable()

def test_TC_011_03_01_verify_the_link_open_manual_is_visible(driver):
    page = PartnersPage(driver)
    page.verify_the_link_open_manual_is_visible()

