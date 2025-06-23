from dataclasses import dataclass

from src.poo.model.Endereco import Endereco

@dataclass
class Usuario:
    nome : str
    email : str
    senha : str
    endereco : Endereco