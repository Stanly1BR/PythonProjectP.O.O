from dataclasses import dataclass

from src.poo.objetos.Endereco import Endereco

@dataclass
class Usuario:
    nome : str
    email : str
    senha : str
    endereco : Endereco