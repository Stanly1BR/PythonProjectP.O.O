from src.poo.objetos.Biblioteca import Biblioteca
from src.poo.objetos.Endereco import Endereco
from unittest.mock import MagicMock

import pytest

from src.poo.objetos.Usuario import Usuario


@pytest.fixture
def endereco_mock():
    return Endereco("12345678", "123")

@pytest.fixture
def usuario_mock(endereco_mock) -> MagicMock:
    usuario_mock = MagicMock(spec=Usuario)
    usuario_mock.nome = "Stanly"
    usuario_mock.email = "<EMAIL>"
    usuario_mock.senha = "<PASSWORD>"
    usuario_mock.endereco = endereco_mock
    return usuario_mock

@pytest.fixture
def biblioteca_mock(endereco_mock):
    return Biblioteca("Biblioteca", endereco_mock)

def test_cadastro_biblioteca(endereco_mock):
    biblioteca = Biblioteca("Biblioteca", endereco_mock)
    assert biblioteca.nome == "Biblioteca"
    assert biblioteca.endereco == endereco_mock


def test_cadastro_usuario(biblioteca_mock, usuario_mock):
    #Teste de cadastro de usuario
    biblioteca_mock.cadastar_usuario(usuario_mock)
    #Verificar se o usuario foi cadastrado no sistema da biblioteca
    assert usuario_mock in biblioteca_mock.usuarios

    # Verifica se os dados do usuario estão corretos
    usuario_mock = biblioteca_mock.usuarios[0]

    assert usuario_mock.nome == "Stanly"
    assert usuario_mock.email == "<EMAIL>"
    assert usuario_mock.senha == "<PASSWORD>"
    assert usuario_mock.endereco.cep == "12345678"
    assert usuario_mock.endereco.numero == "123"




