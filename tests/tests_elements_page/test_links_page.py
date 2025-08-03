import pytest

from pages.elements_page.links_page import LinksPage


@pytest.mark.parametrize("link_text, expected_status", [
    ("Created", "Link has responded with staus 201"),
    ("No Content", "Link has responded with staus 204"),
    ("Moved", "Link has responded with staus 301"),
    ("Bad Request", "Link has responded with staus 400"),
    ("Unauthorized", "Link has responded with staus 401"),
    ("Forbidden", "Link has responded with staus 403"),
    ("Not Found", "Link has responded with staus 404"),
])
def test_api_links(driver, link_text, expected_status):
    driver.get("https://demoqa.com/links")
    page = LinksPage(driver)
    page.click_link_by_text(link_text)
    assert expected_status in page.get_response_text()
