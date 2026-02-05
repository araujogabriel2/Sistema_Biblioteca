
from modelos.biblioteca import Biblioteca
from interface.menus import executar_menu
from dados import acervo_inicial
import os 

def inicializar_sistema():
    sistema=Biblioteca()
    for livro in acervo_inicial:
        sistema.cadastrar_livro(livro['titulo'], livro['autor'], livro['ano'])

    return sistema

def main():
    os.system('cls')
    minha_biblioteca= inicializar_sistema()
    os.system('cls')
    executar_menu(minha_biblioteca)
    
if __name__ == "__main__":
    main()









