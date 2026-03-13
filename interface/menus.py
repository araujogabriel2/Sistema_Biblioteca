from modelos.biblioteca import Biblioteca
import os

def clear():
    os.system('cls')

def interface_cadastrar_usuario(sistema: Biblioteca):
    clear()
    print('---CADASTRO USUÁRIO ---')

    while True:
        nome=input('Digite seu nome:')
        telefone =input('Digite seu número de telefone, com o (DDD):')

        if not nome.replace(' ', '').isalpha():
            print('ERRO: O nome deve conter apenas letras.')
            continue
        if not telefone.isdigit():
            print('ERRO: Digite apenas números!')
            continue
        if len(telefone) < 10 or len(telefone) > 11:
            print('Erro: O telefone deve ter 10 (residêncial) ou 11 (móvel) dígitos, contando com o DDD!')
            continue

        break

    msg=sistema.cadastrar_usuario(nome, telefone)
    print(msg)
        

def interface_locacao(sistema: Biblioteca):
    clear()
    print('----------------- LOCAÇÃO LIVRO ------------------')
    print('EM DESTAQUE:')
    acervo = sistema.listar_livros()
    
    
    for livro in acervo:
        print(f"ID: {livro.id_livro} | Livro: {livro.titulo} | Autor: {livro.autor}")
    
    print('----------------------------------------------------')

    while True:
        usuario_id = input('Digite o ID do usuário:')
        livro_id = input('Digite o ID do livro:')

        if not usuario_id.isdigit() or not livro_id.isdigit():
            print('ERRO: Digite apenas números para os IDs!')
            continue

        break

    msg = sistema.alugar_livro(int(usuario_id), int(livro_id))
    print(msg)

def interface_devolucao(sistema: Biblioteca):
    clear()
    print('---------------- DEVOLUÇÃO LIVRO -------------------')

    while True:
        id_livro = input('Digite o ID do livro alugado:')

        if not id_livro.isdigit():
            print('Erro: Digite apenas números para os IDs!')
            continue

        break

    msg = sistema.devolver_livro(int(id_livro))
    print(msg)

   
def exibir_emprestimos_ativos(sistema: Biblioteca):
    clear()
    print('---------------- MEUS EMPRÉSTIMOS ATIVOS ----------------')

    while True:
        id_usuario = input('Digite seu ID:')

        if not id_usuario.isdigit():
            print('Erro: Digite apenas números para os IDs!')
            continue

        break

    emprestimos = sistema.buscar_emprestimo_id_usuario(int(id_usuario))
    for emprestimo in emprestimos:
        print(emprestimo)
    
    
    

menus={
    "1":interface_cadastrar_usuario,
    "2":interface_locacao,
    "3":interface_devolucao,
    "4":exibir_emprestimos_ativos
}

def executar_menu(sistema):
    clear()
    while True:

        print('1. Cadastrar usuário')
        print('2. Locar Livro')
        print('3. Devolução')
        print('4. Exibir Meus Empréstimos Ativos')


        opcao=input('Escolha uma opção:')

        if opcao in menus:
            funcao_escolhida=menus[opcao]
            funcao_escolhida(sistema)
        else:
            print('Escolha opções que estão dentro do menu.')
