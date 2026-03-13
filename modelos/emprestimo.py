
class Emprestimo:
    def __init__(self, id_livro, id_usuario, status=1, id_emprestimos=None):
        self.id_livro=id_livro
        self.id_usuario=id_usuario
        self.status= status
        self.id_emprestimos = id_emprestimos
    
    def __str__(self):
        return f'Contrato: {self.id_usuario} - Livro: {self.id_livro}'
    