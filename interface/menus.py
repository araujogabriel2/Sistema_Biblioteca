
def interface_cadastrar_usuario(sistema):
    print('---CADASTRO USUÁRIO ---')
    try:
        nome=input('Digite seu nome:')

        if not nome.isalpha():
            print('ERRO: O nome deve conter apenas letras.')
        else:
            telefone=int(input('Digite seu telefone:'))
            sistema.cadastrar_usuario(nome, telefone)

    except ValueError:
        print('O telefone deve conter apenas números.')

def interface_locacao(sistema):
    print('--- LOCAÇÃO LIVRO ---')

    try:
        
        livro_locacao=input('Digite o nome do livro:')
        id=int(input('Digite o seu ID:'))
        livro_encontrado=sistema.buscar_livro(livro_locacao)
        usuario=sistema.buscar_usuario_id(id)
        sistema.locar(livro_encontrado, usuario)

    except ValueError:
        print('ERRO: ID deve conter números.')

def interface_devolucao(sistema):
    print('--- DEVOLUÇÃO LIVRO ---')

    try:

        livro=input('Digite o nome do livro:')
        id=int(input('Digite o seu ID:'))
        livro_devolucao=sistema.buscar_livro(livro)
        usuario=sistema.buscar_usuario_id(id)
        sistema.devolucao(livro_devolucao, usuario)

    except ValueError:
        print('ERRO: ID deve conter apenas números.')

def exibir_emprestimos_ativos(sistema):
    print('--- EMPRÉSTIMOS ATIVOS ---')
    try:

        id_digitado=int(input('Digite o ID:'))
        sistema.emprestimos_ativos(id_digitado)
     
    except ValueError:
        print('ERRO: ID deve conter apenas números.')

    
menus={
    "1":interface_cadastrar_usuario,
    "2":interface_locacao,
    "3":interface_devolucao,
    "4":exibir_emprestimos_ativos
}

def executar_menu(sistema):
    while True:
        print('1. Cadastrar usuário')
        print('2. Locar Livro')
        print('3. Devolução')
        print('4. Exibir Empréstimos Ativos')


        opcao=input('Escolha uma opção:')

        if opcao in menus:
            funcao_escolhida=menus[opcao]
            funcao_escolhida(sistema)
        else:
            print('Escolha opções que estão dentro do menu.')
