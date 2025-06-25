from dataclasses import dataclass, field

from database import db
from src.poo.exceptions.ObjectAlreadyRegisteredException import ObjectAlreadyRegisteredException
from src.poo.exceptions.ObjectNotFoundException import ObjectNotFoundException
from src.poo.model.Endereco import Endereco
from src.poo.model.Livro import Livro
from src.poo.model.Usuario import Usuario


def conectar_banco():
    try:
        db.connect()
        print("Conectado ao banco de dados!")
        return True
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False

def criar_tabelas():
    try:
        db.create_tables([Usuario, Endereco, Livro])
        print("Tabelas criadas com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao criar as tabelas: {e}")
        return False

def desconectar_banco():
    try:
        db.close()
        print("Desconectado do banco de dados!")
        return True
    except Exception as e:
        print(f"Erro ao desconectar do banco de dados: {e}")
        return False

class Biblioteca:
    def __init__(self, nome : str, endereco : Endereco):
        nome : str
        endereco : Endereco
        conectar_banco()


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