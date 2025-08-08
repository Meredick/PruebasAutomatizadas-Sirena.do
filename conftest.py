import pytest
from utils.driver_factory import create_driver
from pages.login_page import LoginPage
from utils.screenshot import take_screenshot


USER = "meredick.rg@gmail.com"
PASS = "Prueba123"

@pytest.fixture(scope="session")
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(USER, PASS)
    login_page.ensure_logged_in()
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Solo tomar screenshot al final de la ejecución del test
    if report.when == "call":
        driver = item.funcargs.get("driver") or item.funcargs.get("logged_in_driver")
        if driver:
            test_name = item.name
            screenshot_path = take_screenshot(driver, test_name)

            # Adjuntar screenshot al reporte HTML si se usa pytest-html
            if screenshot_path and hasattr(report, "extra"):
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    report.extra.append(pytest_html.extras.png(screenshot_path))