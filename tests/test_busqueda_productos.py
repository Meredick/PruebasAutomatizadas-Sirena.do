import pytest
from pages.busqueda_page import BusquedaPage


def test_busqueda_productos(logged_in_driver):
    driver = logged_in_driver
    busq = BusquedaPage(driver)
    busq.search("arroz")

    assert len(driver.find_elements(*BusquedaPage.RESULTS_CONTAINER)) >= 0