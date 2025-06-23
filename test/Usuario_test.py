import pytest

from src.poo.model.Endereco import Endereco
from src.poo.model.Usuario import Usuario

@pytest.fixture
def endereco_mock():
    endereco = Endereco("12345678", "123")
    return endereco

def test_criar_usuario(endereco_mock):
    usuario = Usuario("Gabriel", "<EMAIL>", "<PASSWORD>", endereco_mock)
    assert usuario.nome == "Gabriel"
    assert usuario.email == "<EMAIL>"
    assert usuario.senha == "<PASSWORD>"
    assert usuario.endereco == endereco_mock
