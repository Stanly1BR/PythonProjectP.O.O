from dataclasses import dataclass, field

from src.poo.Livro import Livro
from src.poo.Usuario import Usuario


@dataclass
class Biblioteca:
    nome : str
    endereco : str
    usuarios : list[Usuario] = field(default_factory=list)
    livros : list[Livro] = field(default_factory=list)

    def cadastar(objeto):
        pass

    def remover(objeto):
        pass

    def listar(objeto):
        pass

    def buscar(objeto):
        pass