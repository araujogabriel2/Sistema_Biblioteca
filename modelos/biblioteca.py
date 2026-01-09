
from modelos.emprestimo import Emprestimo
from modelos.livro import Livro
from modelos.usuario import Usuario


class Biblioteca():
    def __init__(self):
        self.emprestimos=[]
        self.lista=[]
        self.usuarios=[]
    

    def cadastrar_usario(self, nome, telefone):
        novo_id=len(self.usuarios) + 1
        novo_usuario=Usuario(nome, telefone, novo_id)
        self.usuarios.append(novo_usuario)
        print(f'Usuário {nome} cadastrado com sucesso! Novo ID: {novo_id} ')


    def emprestar(self, livro, usuario):
        if livro.disponivel:
            livro.disponivel=False
            contrato= Emprestimo(livro, usuario)
            usuario.historico.append(contrato)
            self.emprestimos.append(contrato)
            print(f'{livro.titulo} emprestado para {usuario.nome}')
        else:
            print(f'O livro não está disponível.')


    def devolver(self, livro, usuario):

        for contrato in usuario.historico:
            if contrato.livro == livro:
                livro.disponivel=True
                print(f'Livro: {livro.titulo} devolvido com sucesso!')
                break

    
    def emprestimos_ativos(self):

        print('Lista de emprestimos ativos:')
        for emprestimo in self.emprestimos:
            print(emprestimo)


    def cadastrar_livro(self, titulo, autor, ano):
        livro=Livro(titulo, autor, ano)
        self.lista.append(livro)
        print(f'Livro {titulo} cadastrado!')


   



