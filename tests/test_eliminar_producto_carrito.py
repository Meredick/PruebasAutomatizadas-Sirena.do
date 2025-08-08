import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.carrito_page import CarritoPage
from pages.carrito_page import CarritoPage


def test_eliminar_producto_carrito(logged_in_driver):
    driver = logged_in_driver
    carrito = CarritoPage(driver)
    carrito.open_cart()
    initial_count = carrito.get_items_count()
    initial = carrito.get_items_count()
    if initial == 0:
        pytest.skip("No hay items en el carrito para eliminar — agregar manualmente o revisar test previo")
    carrito.remove_first_item()
    wait = WebDriverWait(driver, 10)
    wait.until(lambda d: carrito.get_items_count() < initial_count)    
    final_count = carrito.get_items_count()
    
    assert final_count == initial_count - 1