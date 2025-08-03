import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # veya Firefox
    driver.maximize_window()
    yield driver
    driver.quit()
