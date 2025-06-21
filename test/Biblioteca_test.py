from src.poo.exceptions.ObjectAlreadyRegisteredException import ObjectAlreadyRegisteredException
from src.poo.exceptions.ObjectNotFoundException import ObjectNotFoundException
from src.poo.objetos.Biblioteca import Biblioteca
from src.poo.objetos.Endereco import Endereco
from unittest.mock import MagicMock

import pytest

from src.poo.objetos.Livro import Livro
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
def livro_mock()-> MagicMock:
    livro_mock = MagicMock(spec=Livro)
    livro_mock.titulo = "O Deus que destroi sonhos!"
    livro_mock.autor = "seila"
    livro_mock.ano = 2023
    return livro_mock


@pytest.fixture
def biblioteca_mock(endereco_mock):
    return Biblioteca("Biblioteca", endereco_mock)

def test_cadastro_biblioteca(endereco_mock):
    biblioteca = Biblioteca("Biblioteca", endereco_mock)
    assert biblioteca.nome == "Biblioteca"
    assert biblioteca.endereco == endereco_mock


def test_cadastro_objeto_usuario(biblioteca_mock, usuario_mock):
    #Teste de cadastro de usuario
    biblioteca_mock.cadastar_objeto(biblioteca_mock.usuarios, usuario_mock)
    #Verificar se o usuario foi cadastrado no sistema da biblioteca
    assert usuario_mock in biblioteca_mock.usuarios

    # Verifica se os dados do usuario estão corretos
    usuario_mock = biblioteca_mock.usuarios[0]

    assert usuario_mock.nome == "Stanly"
    assert usuario_mock.email == "<EMAIL>"
    assert usuario_mock.senha == "<PASSWORD>"
    assert usuario_mock.endereco.cep == "12345678"
    assert usuario_mock.endereco.numero == "123"

def test_cadastro_objeto_livro(biblioteca_mock, livro_mock):

    biblioteca_mock.cadastar_objeto(biblioteca_mock.livros, livro_mock)

    assert livro_mock == biblioteca_mock.livros[0]

    livro_mock = biblioteca_mock.livros[0]

    assert livro_mock.titulo == "O Deus que destroi sonhos!"
    assert livro_mock.autor == "seila"
    assert livro_mock.ano == 2023

def test_cadastro_objeto_usuario_duplicado(biblioteca_mock, usuario_mock):
    # 1. Primeira tentativa de cadastro (deve funcionar)
    biblioteca_mock.cadastar_objeto(biblioteca_mock.usuarios, usuario_mock)

    # 2. Segunda tentativa com o MESMO objeto (deve falhar)
    with pytest.raises(ObjectAlreadyRegisteredException) as e:
        biblioteca_mock.cadastar_objeto(biblioteca_mock.usuarios, usuario_mock)

        # 3. Confirma que continua só com 1 usuario
        assert str(e.value) == f" {usuario_mock} já tem um cadastro!"

def test_cadastro_objeto_livro_duplicado(biblioteca_mock, livro_mock):

    biblioteca_mock.cadastar_objeto(biblioteca_mock.livros, livro_mock)

    with pytest.raises(ObjectAlreadyRegisteredException) as e:
        biblioteca_mock.cadastar_objeto(biblioteca_mock.livros, livro_mock)

        # Opcional: verificar a mensagem da exceção
        assert str(e.value) == f" {livro_mock} já tem um cadastro!"

def test_remover_usuario(biblioteca_mock, usuario_mock):
    biblioteca_mock.cadastar_objeto(biblioteca_mock.usuarios, usuario_mock)
    biblioteca_mock.remover("Stanly", "nome", biblioteca_mock.usuarios)
    assert len(biblioteca_mock.usuarios) == 0

def test_remover_livro(biblioteca_mock, livro_mock):
    biblioteca_mock.cadastar_objeto(biblioteca_mock.livros, livro_mock)
    biblioteca_mock.remover("O Deus que destroi sonhos!", "titulo", biblioteca_mock.livros)
    assert len(biblioteca_mock.livros) == 0

def test_remover_usuario_inexistente(biblioteca_mock, usuario_mock):

    with pytest.raises(ObjectNotFoundException):
        biblioteca_mock.remover("carl", "nome", biblioteca_mock.usuarios)

def test_remover_livro_inexistente(biblioteca_mock, livro_mock):

    with pytest.raises(ObjectNotFoundException):
        biblioteca_mock.remover("carl", "titulo", biblioteca_mock.livros)


def test_listar_usuario(biblioteca_mock, usuario_mock):
    biblioteca_mock.cadastar_objeto(biblioteca_mock.usuarios, usuario_mock)
    biblioteca_mock.listar(biblioteca_mock.usuarios)
    assert len(biblioteca_mock.usuarios) == 1
    assert biblioteca_mock.usuarios[0] == usuario_mock

def test_listar_livro(biblioteca_mock, livro_mock):
    biblioteca_mock.cadastar_objeto(biblioteca_mock.livros, livro_mock)
    biblioteca_mock.listar(biblioteca_mock.livros)
    assert len(biblioteca_mock.livros) == 1
    assert biblioteca_mock.livros[0] == livro_mock

def test_listar_livro_vazio(biblioteca_mock, capsys):
    biblioteca_mock.listar(biblioteca_mock.usuarios)

    # Capturando o que foi impresso

    saida = capsys.readouterr()

    # Verificando a mensagem de lista vazia
    assert "Lista vazia" in saida.out

def test_listar_usuario_vazio(biblioteca_mock, capsys):
    biblioteca_mock.listar(biblioteca_mock.livros)
    saida = capsys.readouterr()
    assert "Lista vazia" in saida.out

def test_buscar_usuario(biblioteca_mock, usuario_mock):
    biblioteca_mock.cadastar_objeto(biblioteca_mock.usuarios, usuario_mock)
    assert biblioteca_mock.buscar(biblioteca_mock.usuarios, "nome", "Stanly") == usuario_mock

def test_buscar_livro(biblioteca_mock, livro_mock):
    biblioteca_mock.cadastar_objeto(biblioteca_mock.livros, livro_mock)
    assert biblioteca_mock.buscar(biblioteca_mock.livros, "titulo", "O Deus que destroi sonhos!") == livro_mock

def test_buscar_usuario_nao_existe(biblioteca_mock, usuario_mock):
    biblioteca_mock.usuarios = []

    resultado = biblioteca_mock.buscar(biblioteca_mock.usuarios, "nome", "carl")
    assert resultado is None

def test_buscar_livro_nao_existe(biblioteca_mock, livro_mock):
    biblioteca_mock.livros = []

    resultado = biblioteca_mock.buscar(biblioteca_mock.usuarios, "nome", "carl")
    assert resultado is None

def test_buscar_sistema_usuario(biblioteca_mock, usuario_mock):
    biblioteca_mock.cadastar_objeto(biblioteca_mock.usuarios, usuario_mock)
    assert biblioteca_mock.buscar_sistema(biblioteca_mock.usuarios, usuario_mock) == True

def test_buscar_sistema_livro(biblioteca_mock, livro_mock):
    biblioteca_mock.cadastar_objeto(biblioteca_mock.livros, livro_mock)
    assert biblioteca_mock.buscar_sistema(biblioteca_mock.livros, livro_mock) == True

def test_buscar_sistema_usuario_nao_existe(biblioteca_mock, usuario_mock):
    assert biblioteca_mock.buscar_sistema(biblioteca_mock.usuarios, usuario_mock) == False

def test_buscar_sistema_livro_nao_existe(biblioteca_mock, livro_mock):
    assert biblioteca_mock.buscar_sistema(biblioteca_mock.livros, livro_mock) == False


