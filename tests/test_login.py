from pages.login_page import LoginPage

def test_login_usuario_registrado(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("meredick.rg@gmail.com", "Prueba123")
    login_page.ensure_logged_in()
    assert True



    