from src.poo.objetos.Usuario import Usuario

def test_criar_usuario():
    usuario = Usuario("Gabriel", "<EMAIL>", "123456", "1234567890")
    assert usuario.nome == "Gabriel"
    assert usuario.email == "<EMAIL>"
    assert usuario.senha == "<PASSWORD>"
    assert usuario.endereco.cep == "1234567890"