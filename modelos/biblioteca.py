from modelos.emprestimo import Emprestimo
from modelos.livro import Livro
from modelos.usuario import Usuario
import json 
import os


class Biblioteca:
    def __init__(self):
        self.emprestimos = []
        self.usuarios = []
        self.livros=[]
        self.carregar_usuarios()
        

    def cadastrar_usuario(self, nome, telefone):
        novo_id = len(self.usuarios) + 1
        novo_usuario = Usuario(nome, telefone, novo_id)
        self.usuarios.append(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso! Novo ID: {novo_id} ")
        self.salvar_usuario()

    def salvar_usuario(self):
        arquivo_json='usuarios.json'
        lista_dicionario=[]

        for objeto in self.usuarios:
            objeto = {
                "NOME": objeto.nome,
                "TELEFONE": objeto.telefone,
                "ID": objeto.id_usuario
            }
            lista_dicionario.append(objeto)
        
        with open(arquivo_json, "w", encoding='utf-8') as arquivo:
            json.dump(lista_dicionario, arquivo, indent=4, ensure_ascii=False)

    def carregar_usuarios(self):
        arquivo_json='usuarios.json'
        if os.path.exists(arquivo_json):
            try:
                with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
                    lista=json.load(arquivo)
                    for dicionario in lista:
                        novo_objeto=Usuario(
                            dicionario["NOME"],
                            dicionario["TELEFONE"],
                            dicionario["ID"]
                        )
                        self.usuarios.append(novo_objeto)
            except json.JSONDecodeError:
                lista=[]
        else:
            lista=[]

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
