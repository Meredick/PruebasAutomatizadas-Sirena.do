from pages.busqueda_page import BusquedaPage
from pages.carrito_page import CarritoPage


def test_agregar_producto_carrito(logged_in_driver):
    driver = logged_in_driver
    busq = BusquedaPage(driver)
    carrito = CarritoPage(driver)

    busq.search("arroz")
    busq.add_first_result_to_cart()

    carrito.open_cart()
    assert carrito.get_items_count() >= 1    