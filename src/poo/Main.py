from src.poo.Biblioteca import Biblioteca
from src.poo.Endereco import Endereco
from src.poo.Livro import Livro
from src.poo.Usuario import Usuario

endereco1 = Endereco("49100044", "Bla bla rua")
endereco2 = Endereco("49100045", "kakakak rua")

biblioteca = Biblioteca("Book", endereco1)

usuario1 = Usuario("stanly", "stanly@gmail.com", "2837182", endereco2)
livro1 = Livro("O livro", "O autor", 456435)
livro2 = Livro("O livro 2", "O autor 2", 456435)

print("====================================================================")

biblioteca.cadastar_usuario(usuario1)
biblioteca.cadastar_livro(livro1)
biblioteca.cadastar_livro(livro2)

print("====================================================================")

biblioteca.listar_livros()
biblioteca.listar_usuarios()

print("====================================================================")

biblioteca.buscar(biblioteca.livros, "titulo","O livro")

biblioteca.remover_livro(livro1)

print("====================================================================")

biblioteca.listar_livros()

