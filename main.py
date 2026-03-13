
from modelos.biblioteca import Biblioteca
from interface.menus import executar_menu
from dados import acervo_inicial
import os


def inicializar_sistema(acervo_inicial):
    sistema=Biblioteca()
    for livro in acervo_inicial:
        msg=sistema.cadastrar_livro(livro['titulo'], livro['autor'], livro['ano'])
        print(f'tentativa com {livro['titulo']} : {msg}')

    return sistema

def main():
    os.system('cls')
    minha_biblioteca= inicializar_sistema(acervo_inicial)
    executar_menu(minha_biblioteca)
    
if __name__ == "__main__":
    main()









