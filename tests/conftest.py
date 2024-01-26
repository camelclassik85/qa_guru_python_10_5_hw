import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser.config.base_url = 'https://demoqa.com/'
    browser.config.driver_name = 'firefox'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()
