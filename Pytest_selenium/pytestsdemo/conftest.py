import os
import pytest
import pytest_html
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
    global driver
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=chrome_options)
    if browser_name == "Firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    if browser_name == "edge":
        service_obj = Service("/Pytest_selenium/selenium_scripts/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        driver.maximize_window()

    yield driver
    driver.quit()

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    Pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(Pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)

def pytest_html_report_title(report):
    report.title = "Automation report"


@pytest.fixture()
def dataload():
    return ["Jeeva", "Reshma", "krithik", "jeevareshkrithik.com"]


@pytest.fixture(params=["Google", "FireFox", "IE"])
def crossbrowser(request):
    return request.param


