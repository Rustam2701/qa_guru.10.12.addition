import pytest

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def configuration_browser(browser=None):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
