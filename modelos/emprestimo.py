
class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro=livro
        self.usuario=usuario
        self.status='Ativo'
    
    def __str__(self):
        return f'Contrato: {self.usuario} - Livro: {self.livro}'
    