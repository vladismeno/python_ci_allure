import allure
import allure_commons
import pytest
from selene import browser, support
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser_management(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--headless=new')
    options.add_argument("--lang=en")
    browser.config.driver_options = options

    browser.config.timeout = 3
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )
    failed_before = request.session.testsfailed

    yield

    if request.session.testsfailed != failed_before:
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    browser.quit()