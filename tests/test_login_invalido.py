from pages.login_page import LoginPage

def test_login_invalido(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("usuario_invalido@example.com", "clave_erronea")
    error_message = login_page.get_error_message()
    assert "el usuario y/o contraseña que has introducido no es la correcta" in error_message.lower() or "inválido" in error_message.lower()
