from dataclasses import dataclass

from src.poo.Endereco import Endereco


@dataclass
class Usuario:
    nome : str
    sobrenome : str
    email : str
    senha : str
    endereco : Endereco