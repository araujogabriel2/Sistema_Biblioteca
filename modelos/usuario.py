
class Usuario:
    def __init__(self, nome, telefone, id_usuario=None):
        self.nome = nome
        self.telefone = telefone
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Nome: {self.nome}"

