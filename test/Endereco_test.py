from src.poo.objetos.Endereco import Endereco

def test_criar_objeto():
    endereco = Endereco("12345678", "123")
    assert endereco.cep == "12345678"
    assert endereco.numero == "123"