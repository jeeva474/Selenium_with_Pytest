import os
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser selection"
    )


@pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=options)

    elif browser_name.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = os.path.join(
                screenshot_dir, f"{item.name}.png"
            )
            driver.save_screenshot(file_name)


def _capture_screenshot(file_name):
    driver = globals().get("driver")
    if driver:
        driver.get_screenshot_as_file(file_name)

def pytest_html_report_title(report):
    report.title = "Automation report"


@pytest.fixture()
def dataload():
    return ["Jeeva", "Reshma", "krithik", "jeevareshkrithik.com"]


@pytest.fixture(params=["Google", "FireFox", "IE"])
def crossbrowser(request):
    return request.param
