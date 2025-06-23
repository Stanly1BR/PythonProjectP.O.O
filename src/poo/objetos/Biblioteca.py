from dataclasses import dataclass, field

from src.poo.exceptions.ObjectAlreadyRegisteredException import ObjectAlreadyRegisteredException
from src.poo.exceptions.ObjectNotFoundException import ObjectNotFoundException
from src.poo.model.Endereco import Endereco
from src.poo.model.Livro import Livro
from src.poo.model.Usuario import Usuario


@dataclass
class Biblioteca:
    nome : str
    endereco : Endereco
    usuarios : list[Usuario] = field(default_factory=list)
    livros : list[Livro] = field(default_factory=list)

    def cadastar_objeto(self, tipo_objeto, objeto):
        if self.buscar_sistema(tipo_objeto, objeto):
            raise ObjectAlreadyRegisteredException(f" {objeto} já tem um cadastro!")
        else:
            tipo_objeto.append(objeto)
            print(f"{objeto} cadastrado com sucesso!")

    @staticmethod
    def remover(nome_busca, chave, objeto):
        encontrou = False
        for i in objeto:
            if getattr(i, chave) == nome_busca:
                objeto.remove(i)
                print(f"{i} removido com sucesso!")
                encontrou = True
                break
        if not encontrou:
            raise ObjectNotFoundException(f" {nome_busca} não tem cadastro!")

    @staticmethod
    def listar(objeto):
        if len(objeto) == 0:
            print("Lista vazia")
        else:
            for objeto in objeto:
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