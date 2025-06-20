from dataclasses import dataclass, field

from src.poo.Endereco import Endereco
from src.poo.Livro import Livro
from src.poo.Usuario import Usuario


@dataclass
class Biblioteca:
    nome : str
    endereco : Endereco
    usuarios : list[Usuario] = field(default_factory=list)
    livros : list[Livro] = field(default_factory=list)

    def cadastar_usuario(self, objeto : Usuario):
        self.usuarios.append(objeto)

    def cadastar_livro(self, objeto : Livro):
        self.livros.append(objeto)

    def remover_usuario(self, objeto : Usuario):
        self.usuarios.remove(objeto)

    def remover_livro(self, objeto : Livro):
        self.livros.remove(objeto)

    def listar_usuarios(self):
        for objeto in self.usuarios:
            print(objeto)

    def listar_livros(self):
        for objeto in self.livros:
            print(objeto)

    def buscar(self, objeto, chave, chave_nome):

        for item in objeto:
            if getattr(item, chave) == chave_nome:
                print(item)
                return item
        print("Não constar no sistema")
        return None