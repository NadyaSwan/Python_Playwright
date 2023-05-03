from pages.login_page import LoginPage
from pages.product_list_page import ProductListPage
from playwright.sync_api import Page, expect

PASSWORD = 'secret_sauce'


def test_login_with_correct_credentials(page: Page):
    login_page = LoginPage(page)
    product_list_page = ProductListPage(page)

    login_page.log_in('standard_user', PASSWORD)

    expect(login_page.username_input()).not_to_be_visible()
    expect((product_list_page.title_header())).to_be_visible()
    expect((product_list_page.title_header())).to_have_text(product_list_page.HEADER_TEXT)


def test_login_with_incorrect_credentials(page: Page):
    login_page = LoginPage(page)
    product_list_page = ProductListPage(page)

    login_page.log_in('invalid_username', PASSWORD)

    expect(login_page.username_input()).to_be_visible()
    expect(login_page.login_error_label()).to_be_visible()
    expect((login_page.login_error_label())).to_have_text(login_page.INVALID_CREDENTIALS_ERROR_TEXT)
    expect((product_list_page.title_header())).not_to_be_visible()


def test_login_with_locked_out_user(page: Page):
    login_page = LoginPage(page)
    product_list_page = ProductListPage(page)

    login_page.log_in('locked_out_user', PASSWORD)

    expect(login_page.username_input()).to_be_visible()
    expect(login_page.login_error_label()).to_be_visible()
    expect((login_page.login_error_label())).to_have_text(login_page.LOCKED_USER_ERROR_TEXT)
    expect((product_list_page.title_header())).not_to_be_visible()
