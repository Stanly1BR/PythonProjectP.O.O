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
        if not db.is_closed():
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
        if conectar_banco():
            criar_tabelas()


    def cadastar_objeto(self, tipo_objeto, objeto_data):
        try:
            if tipo_objeto == Usuario:
                if Usuario.select().where(Usuario.email == objeto_data.email).exists():
                    raise ObjectAlreadyRegisteredException(
                        f"Usuário com email '{objeto_data.email}' já tem um cadastro!")

                endereco_obj, created = Endereco.get_or_create(
                    cep=objeto_data["endereco"]["cep"],
                    numero=objeto_data["endereco"]["numero"]
                    )

                usuario_obj = Usuario.create(
                    nome=objeto_data["nome"],
                    email=objeto_data["email"],
                    senha=objeto_data["senha"],
                    endereco=endereco_obj
                )

                print(f"Usuário '{usuario_obj.nome}' cadastrado com sucesso!")
                return usuario_obj

            elif tipo_objeto == Livro:
                if Livro.select().where(
                        (Livro.titulo == objeto_data.titulo) & (Livro.autor == objeto_data.autor)).exists():
                    raise ObjectAlreadyRegisteredException(
                        f"Livro '{objeto_data.titulo}' por '{objeto_data.autor}' já tem um cadastro!")

                livro_db = Livro.create(
                    titulo=objeto_data["titulo"],
                    autor=objeto_data["autor"],
                    ano=objeto_data["ano"]
                )

                print(f"Livro '{livro_db.titulo}' cadastrado com sucesso!")
                return livro_db
            else:
                raise ValueError("Tipo de objeto não suportado para cadastro.")
        except Exception as e:
            raise e


    def remover(self,tipo_objeto, chave, valor_chave):
        try:
            query = tipo_objeto.delete().where(getattr(tipo_objeto, chave) == valor_chave)
            rows_deleted = query.execute()
            if rows_deleted > 0:
                print(f"'{valor_chave}' removido com sucesso!")
            else:
                raise ObjectNotFoundException(f"'{valor_chave}' não encontrado para remoção.")
        except Exception as e:
            raise e


    def listar(self, tipo_objeto):
        try:
            records = tipo_objeto.select()
            if not records.count():
                print(f"Nenhum {tipo_objeto.__name__} cadastrado.")
            else:
                for record in records:
                    print(record)
            return list(records)
        except Exception as e:
            print(f"Erro ao listar {tipo_objeto.__name__}: {e}")
            return []


    def buscar(self, tipo_objeto, chave, valor_chave):
        try:
            query = tipo_objeto.select().where(getattr(tipo_objeto, chave) == valor_chave)
            found_object = query.first()
            if found_object:
                print(found_object)
                return found_object
            else:
                print(f"'{valor_chave}' não encontrado.")
                return None
        except Exception as e:
            print(f"Erro ao buscar {tipo_objeto.__name__}: {e}")
            return None

    @staticmethod
    def buscar_sistema(objeto, novo_objeto):
        for item in objeto:
            if item == novo_objeto:
                return True
        return False