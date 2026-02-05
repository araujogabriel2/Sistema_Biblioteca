class Usuario:
    def __init__(self, nome, telefone, id_usuario):
        self.nome = nome
        self.telefone = telefone
        self.id_usuario = id_usuario
        self.historico = []

    def __str__(self):
        return f"Nome: {self.nome}"

    def exibir_livros_alugados(self):
        print(f"Lista de livros alugados - Nome: {self.nome} - ID: {self.id_usuario}")
        for livro in self.historico:
            print(livro)
