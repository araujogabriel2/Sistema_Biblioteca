from modelos.emprestimo import Emprestimo
from modelos.livro import Livro
from modelos.usuario import Usuario


class Biblioteca:
    def __init__(self):
        self.emprestimos = []
        self.usuarios = []
        self.livros=[]

    def cadastrar_usuario(self, nome, telefone):
        novo_id = len(self.usuarios) + 1
        novo_usuario = Usuario(nome, telefone, novo_id)
        self.usuarios.append(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso! Novo ID: {novo_id} ")

    def cadastrar_livro(self, titulo, autor, ano):
        novo_livro=Livro(titulo, autor, ano)
        self.livros.append(novo_livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    def buscar_usuario_id(self, id):
        for usuario in self.usuarios:
            if str(usuario.id_usuario) == str(id):
                return usuario
            else:
                None

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
            else: 
                None

    def locar(self, livro, usuario):

        if usuario in self.usuarios:
                        
            if livro.disponivel:
                livro.disponivel = False
                contrato = Emprestimo(livro, usuario)
                usuario.historico.append(contrato)
                self.emprestimos.append(contrato)
                print(f"{livro.titulo} emprestado para {usuario.nome}")
            else:
                print(f"O livro não está disponível.")

        else:
            print('É necessário um cadastro para locar um livro.')
            nome=input('Digite seu nome:')
            tel=input('Digite seu telefone:')
            self.cadastrar_usuario(nome, tel)

    def devolucao(self, livro, usuario):

        if usuario in self.usuarios:
            for contrato in usuario.historico:
                if contrato.livro == livro:
                    livro.disponivel = True
                    print(f"Livro: {livro.titulo} devolvido com sucesso!")
                    break
                else:
                    print('Livro já devolvido ou não foi alugado por este usuário.')
        else:
            print('ID não cadastrado!')
            nome=input('Digite seu nome:')
            tel=input('Digite seu telefone:')
            self.cadastrar_usuario(nome, tel)

    def emprestimos_ativos(self, id_usuario):
        usuario_encontrado=self.buscar_usuario_id(id_usuario)

        if usuario_encontrado:
            print(f'Histórico de {usuario_encontrado.nome}')

            for emprestimo in usuario_encontrado.historico:
                print(emprestimo)

       

    def verificador_usuario(self, id):
        for usuario in self.usuarios:
            
            if str(usuario.id_usuario) == str(id):
                return usuario

            else:
                return None
