from src.poo.objetos.Endereco import Endereco
from src.poo.objetos.Usuario import Usuario


def test_criar_objeto_endereco():
    endereco = Endereco("12345678", "123")
    assert endereco.cep == "12345678"
    assert endereco.numero == "123"

def test_criar_usuario():
    endereco = Endereco("12345678", "123")
    usuario = Usuario("Gabriel", "<EMAIL>", "<PASSWORD>", endereco)
    assert usuario.nome == "Gabriel"
    assert usuario.email == "<EMAIL>"
    assert usuario.senha == "<PASSWORD>"
    assert usuario.endereco == Endereco("12345678", "123")
