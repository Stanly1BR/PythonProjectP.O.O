import os

from src.poo.exceptions.ObjectAlreadyRegisteredException import ObjectAlreadyRegisteredException
from src.poo.exceptions.ObjectNotFoundException import ObjectNotFoundException
from src.poo.objetos.Biblioteca import Biblioteca, desconectar_banco
from src.poo.model.Endereco import Endereco
from src.poo.model.Livro import Livro
from src.poo.model.Usuario import Usuario

biblioteca = Biblioteca("Biblioteca", Endereco(cep="12345678", numero="123"))

def menu() -> None:
    print("=======================")
    print("========MENU===========")
    print("=======================")
    print("1 - Usuario")
    print("2 - Livro")
    print("0 - Sair")
    print("=======================")
    print("Digite a opção desejada:")
    
def menu_usuario() -> None:
    print("=======================")
    print("=====MENU USUARIO=====")
    print("=======================")
    print("1 - Cadastrar usuario")
    print("2 - Listar usuarios")
    print("3 - Buscar usuario")
    print("4 - Remover usuario")
    print("5 - voltar")
    print("=======================")
    print("Digite a opção desejada:")
    
def menu_livro() -> None:
    print("=======================")
    print("=====MENU LIVRO=======")
    print("=======================")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Remover livro")
    print("5 - voltar")
    print("=======================")
    print("Digite a opção desejada:")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_entrada(entrada, valor_min, valor_max ):
    if entrada <valor_min or entrada > valor_max:
        raise ValueError


while True:
    limpar_terminal()
    menu()
    opcao = 0

    try:
        opcao = int(input())
        validar_entrada(opcao, 0,2)
    except ValueError as e:
        print(f"Erro de entrada: {e}")
        continue
    except Exception as E:
        print(f"Ocorreu um erro inesperado: {E}")
        continue

    if opcao == 0:
        desconectar_banco()
        break

    if opcao == 1:
        limpar_terminal()
        menu_usuario()

        try:
            opcao_usuario = int(input())
            validar_entrada(opcao_usuario, 1, 5)

            if opcao_usuario == 1:
                nome = str(input("Digite o nome do usuario: "))
                email = str(input("Digite o email do usuario: "))
                senha = str(input("Digite a senha do usuario: "))
                cep = str(input("Digite o cep do usuario: "))
                numero = str(input("Digite o numero do usuario: "))

                # Cria um dicionário para os dados do endereço
                endereco = {
                    "cep": cep,
                    "numero": numero
                }
                # Cria um dicionário para os dados do usuário, incluindo o endereço
                usuario_novo = {
                    "nome": nome,
                    "email": email,
                    "senha": senha,
                    "endereco": endereco  # Passa o dicionário de endereço
                }

                biblioteca.cadastar_objeto(Usuario, usuario_novo)

            elif opcao_usuario == 2:
                biblioteca.listar(Usuario)

            elif opcao_usuario == 3:
                buscar_por_nome = str(input("Digite o nome do usuario: "))
                biblioteca.buscar(Usuario, "nome", buscar_por_nome)

            elif opcao_usuario == 4:
                nome = str(input("Digite o nome do usuario: "))
                biblioteca.remover(Usuario, "nome", nome)

        except ObjectAlreadyRegisteredException as e:
            print(f"Ocorreu um erro de cadastro de usuario: {e}")
        except ObjectNotFoundException as e:
            print(f"Erro ao remover/buscar usuario: {e}")
        except ValueError as e:
            print(f"Ocorreu um erro de valores dentro do menu usuario: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

    if opcao == 2:
        limpar_terminal()
        menu_livro()

        try:
            opcao_livro = int(input())
            validar_entrada(opcao_livro, 1, 5)

            if opcao_livro == 1:
                titulo = str(input("Digite o titulo do livro: "))
                autor = str(input("Digite o autor do livro: "))
                ano = str(input("Digite o ano do livro: "))

                # Cria um dicionário para os dados do livro
                livro_novo = {
                    "titulo": titulo,
                    "autor": autor,
                    "ano": ano
                }

                biblioteca.cadastar_objeto(Livro, livro_novo)

            elif opcao_livro == 2:
                biblioteca.listar(Livro)

            elif opcao_livro == 3:
                buscar_por_titulo = str(input("Digite o titulo do livro: "))
                biblioteca.buscar(Livro, "titulo", buscar_por_titulo)

            elif opcao_livro == 4:
                titulo = str(input("Digite o titulo do livro: "))
                biblioteca.remover(Livro, "titulo", titulo)

        except ObjectAlreadyRegisteredException as e:
            print(f"Ocorreu um erro de cadastro de livro: {e}")
        except ObjectNotFoundException as e:
            print(f"Erro ao remover/buscar livro: {e}")
        except ValueError as e:
            print(f"Ocorreu um erro de valores dentro do menu livro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
