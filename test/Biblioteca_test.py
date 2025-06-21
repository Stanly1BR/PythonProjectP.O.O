from src.poo.objetos.Biblioteca import Biblioteca

def test_cadastro_biblioteca():
    biblioteca = Biblioteca("Biblioteca", "12345678", "123")
    assert biblioteca.nome == "Biblioteca"
