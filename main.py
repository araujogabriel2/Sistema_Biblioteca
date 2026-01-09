from modelos.livro import Livro
from modelos.usuario import Usuario
from modelos.biblioteca import Biblioteca
import os


def main():
    
    print(f'𝚂𝚒𝚜𝚝𝚎𝚖𝚊 𝙱𝚒𝚋𝚕𝚒𝚘𝚝𝚎𝚌𝚊')
    print('')
    minha_biblioteca=Biblioteca()

    print(f'1. Cadastrar Usuário:\n2.Cadastrar Livro:')
    print('')
     
    entrada=input('Digite um número para o seu respectivo comando:')

    if entrada == '1':
        nome=input('Digite seu nome:')
        telefone=input('Digite seu telefone:')
        minha_biblioteca.cadastrar_usario(nome, telefone)
        





if __name__ == "__main__":
    main()









