📚 Visão Geral do Projeto
Este é um sistema simples de gerenciamento de biblioteca desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos (POO). O objetivo é simular as operações básicas de uma biblioteca, como cadastro de usuários e livros, listagem, busca e remoção. O projeto foi estruturado para demonstrar boas práticas de organização de código, tratamento de exceções e uso de dataclasses.

✨ Funcionalidades
O sistema oferece as seguintes funcionalidades principais através de um menu interativo:

Gerenciamento de Usuários:
Cadastrar novos usuários (com nome, email, senha e endereço).
Listar todos os usuários cadastrados.
Buscar usuários por nome.
Remover usuários cadastrados.
Gerenciamento de Livros:
Cadastrar novos livros (com título, autor e ano).
Listar todos os livros cadastrados.
Buscar livros por título.
Remover livros cadastrados.


Estrutura de Pastas:
Certifique-se de que a estrutura de pastas do projeto esteja como a seguinte:

### Estrutura de Pastas

O projeto segue uma estrutura modular para organizar o código de forma clara:

```text
PythonProjectP.O.O/
├── src/
│   └── poo/
│       ├── exceptions/
│       │   ├── ObjectAlreadyRegisteredException.py
│       │   └── ObjectNotFoundException.py
|       ├── model/
│       │   ├── Usuario.py
|       |   ├── Livro.py
|       |   └── Endereco.py
│       └── objetos/
│           └── Biblioteca.py
└── Main.py
```

Execução
A partir da raiz do projeto (PythonProjectP.O.O/), execute o arquivo Main.py:

💻 Estrutura e Design do Algoritmo
O projeto é construído com uma abordagem clara de Programação Orientada a Objetos, dividida em módulos para melhor organização:

src/poo/objetos/: Contém as definições das classes de modelo de dados e a classe principal da biblioteca.

Endereco.py: Uma dataclass simples para representar um endereço com cep e numero.
Usuario.py: Uma dataclass que define um usuário com nome, email, senha e um objeto Endereco.
Livro.py: Uma dataclass para representar um livro com titulo, autor e ano de publicação.
Biblioteca.py: A classe central do sistema.
Gerencia listas de Usuario e Livro.
Implementa métodos para cadastrar, listar, buscar e remover usuários e livros.
Utiliza dataclasses para simplificar a criação de objetos.
Contém um método estático buscar_sistema que verifica a existência de um objeto em uma coleção.
Possui um método estático buscar para encontrar um objeto pelo valor de um atributo específico (ex: nome do usuário, título do livro).
src/poo/exceptions/: Contém classes de exceção personalizadas para lidar com cenários específicos do domínio.

ObjectAlreadyRegisteredException.py: Levantada quando se tenta cadastrar um objeto que já existe.
ObjectNotFoundException.py: Levantada quando se tenta buscar ou remover um objeto que não foi encontrado.
Main.py: O ponto de entrada do programa.

Contém a lógica do menu interativo para o usuário.
Cria uma instância da Biblioteca e interage com seus métodos.
Inclui funções auxiliares como limpar_terminal() e validar_entrada() para melhorar a experiência do usuário.
Implementa tratamento de exceções (try-except) para gerenciar erros de entrada e exceções personalizadas da Biblioteca.
