from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BusquedaPage:
    SEARCH_INPUT = (By.ID, "search-main-input")
    SEARCH_BUTTON = (By.CLASS_NAME, "uk-search-icon uk-search-icon-flip")
    RESULTS_CONTAINER = (By.CSS_SELECTOR, "div[data-test='grid-product']")
    FIRST_PRODUCT_ADD = (By.ID, "btn-add-to-cart")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def search(self, term: str):
        search_input = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(term)
        try:
            btn = self.driver.find_element(*self.SEARCH_BUTTON)
            btn.click()
        except Exception:
            search_input.send_keys('\n')
        self.wait.until(EC.visibility_of_element_located(self.RESULTS_CONTAINER))

    def add_first_result_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_PRODUCT_ADD)).click()