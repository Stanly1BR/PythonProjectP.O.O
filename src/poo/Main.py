import os

from src.poo.exceptions.ObjectAlreadyRegisteredException import ObjectAlreadyRegisteredException
from src.poo.objetos.Biblioteca import Biblioteca
from src.poo.objetos.Endereco import Endereco
from src.poo.objetos.Livro import Livro
from src.poo.objetos.Usuario import Usuario

biblioteca = Biblioteca("Biblioteca", Endereco("12345678", "123"))

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

    except Exception as E:
        print(f"Ocorreu um erro inesperado: {E}")
        continue

    if opcao == 0:
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

                endereco_novo = Endereco(cep, numero)
                usuario_novo = Usuario(nome, email, senha, endereco_novo)

                biblioteca.cadastar_objeto(biblioteca.usuarios,usuario_novo)

            elif opcao_usuario == 2:
                biblioteca.listar(biblioteca.usuarios)

            elif opcao_usuario == 3:
                buscar_por_nome = str(input("Digite o nome do usuario: "))
                biblioteca.buscar(biblioteca.usuarios, "nome", buscar_por_nome)

            elif opcao_usuario == 4:
                nome = str(input("Digite o nome do usuario: "))
                biblioteca.remover(nome, "nome", biblioteca.usuarios)

        except ObjectAlreadyRegisteredException as e:
            print(f"Ocorreu um erro de cadastro de usuario: {e}")
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
                ano = int(input("Digite o ano do livro: "))

                livro_novo = Livro(titulo, autor, ano)
                biblioteca.cadastar_objeto(biblioteca.livros, livro_novo)

            elif opcao_livro == 2:
                biblioteca.listar(biblioteca.livros)

            elif opcao_livro == 3:
                buscar_por_titulo = str(input("Digite o titulo do livro: "))
                biblioteca.buscar(biblioteca.livros, "titulo", buscar_por_titulo)

            elif opcao_livro == 4:
                titulo = str(input("Digite o titulo do livro: "))
                biblioteca.remover(biblioteca.livros, "titulo", titulo)

        except ObjectAlreadyRegisteredException as e:
            print(f"Ocorreu um erro de cadastro de livro: {e}")
        except ValueError as e:
            print(f"Ocorreu um erro de valores dentro do menu livro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
