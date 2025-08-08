from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CarritoPage:
    CART_BUTTON = (By.ID, "btn-cart")
    CART_ITEM_ROWS = (By.CSS_SELECTOR, "div.cart-list-item")
    REMOVE_BUTTON_IN_ROW = (By.ID, "remove-item-cartbar")
    EMPTY_CART_MSG = (By.XPATH, "//h4[text()='El carrito está vacío.']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CART_BUTTON)).click()
        self.wait.until(EC.visibility_of_all_elements_located(self.CART_ITEM_ROWS))

    def get_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEM_ROWS)
        return len(items)

    def remove_first_item(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.REMOVE_BUTTON_IN_ROW))
        btn.click()
        # esperar que la lista se actualice
        self.wait.until(lambda d: len(d.find_elements(*self.CART_ITEM_ROWS)) < 1 or d.find_elements(*self.EMPTY_CART_MSG))