from src.poo.objetos.Livro import Livro

def test_criar_objeto():
    livro = Livro("O livro", "Gabriel", 2021)
    assert livro.titulo == "O livro"
    assert livro.autor == "Gabriel"
    assert livro.ano == 2021