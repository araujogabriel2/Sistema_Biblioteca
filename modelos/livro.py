class Livro:
    def __init__(self, id_livro, titulo, autor, ano, disponivel=None):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def __str__(self):
        return f" ID:{self.id_livro} - {self.titulo} - {self.autor} - {self.ano}"

   