from pages.carrito_page import CarritoPage


def test_visualizar_productos_carrito(logged_in_driver):
    driver = logged_in_driver
    carrito = CarritoPage(driver)
    carrito.open_cart()
    assert carrito.get_items_count() >= 1