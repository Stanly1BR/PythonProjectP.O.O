from dataclasses import dataclass, field

from src.poo.exceptions.ObjectAlreadyRegisteredException import ObjectAlreadyRegisteredException
from src.poo.exceptions.ObjectNotFoundException import ObjectNotFoundException
from src.poo.objetos.Endereco import Endereco
from src.poo.objetos.Livro import Livro
from src.poo.objetos.Usuario import Usuario


@dataclass
class Biblioteca:
    nome : str
    endereco : Endereco
    usuarios : list[Usuario] = field(default_factory=list)
    livros : list[Livro] = field(default_factory=list)

    def cadastar_usuario(self, objeto : Usuario):
        if self.buscar_sistema(self.usuarios, objeto):
            raise ObjectAlreadyRegisteredException(f"Usuario {objeto} já tem um cadastro!")
        else:
            self.usuarios.append(objeto)
            print(f"Usuario {objeto} cadastrado com sucesso!")

    def cadastar_livro(self, objeto : Livro):
        if self.buscar_sistema(self.livros, objeto):
            raise ObjectAlreadyRegisteredException(f"Livro {objeto} já tem um cadastro!")
        else:
            self.livros.append(objeto)
            print(f"Livro {objeto} cadastrado com sucesso!")

    def remover_usuario(self, nome_busca):
        encontrou = False
        for i in self.usuarios:
            if i.nome == nome_busca:
                self.usuarios.remove(i)
                print(f"Usuario {i} removido com sucesso!")
                encontrou = True
                break
        if not encontrou:
            raise ObjectNotFoundException(f"Usuario {nome_busca} não tem cadastro!")

    def remover_livro(self, nome_busca):
        encontrou = False
        for i in self.livros:
            if i.titulo == nome_busca:
                self.livros.remove(i)
                print(f"Livro {i} removido com sucesso!")
                encontrou = True
                break
        if not encontrou:
            raise ObjectNotFoundException(f"Livro {nome_busca} não tem cadastro!")

    def listar_usuarios(self):
        if len(self.usuarios) == 0:
            print("Lista de Usuarios vazia")
        else:
            for objeto in self.usuarios:
                print(objeto)

    def listar_livros(self):
        if len(self.livros) == 0:
            print("Lista de Livros vazia")
        else:
            for objeto in self.livros:
                print(objeto)

    @staticmethod
    def buscar(objeto, chave, chave_nome):

        for item in objeto:
            if getattr(item, chave) == chave_nome:
                print(item)
                return item
        return None

    @staticmethod
    def buscar_sistema(objeto, novo_objeto):
        for item in objeto:
            if item == novo_objeto:
                return True
        return False