
def interface_cadastrar_usuario(sistema):
    print('---CADASTRO USUÁRIO ---')
    nome=input('Digite seu nome:')
    telefone=input('Digite seu telefone:')
    sistema.cadastrar_usuario(nome, telefone)

def interface_locacao(sistema):
    print('--- LOCAÇÃO LIVRO ---')
    livro=input('Digite o nome do livro:')
    id=input('Digite o seu ID:')

    livro_encontrado=sistema.buscar_livro(livro)
    usuario=sistema.buscar_usuario_id(id)
    sistema.locar(livro_encontrado, usuario)
    
menus={
    "1":interface_cadastrar_usuario,
    "2":interface_locacao
}

def executar_menu(sistema):
    while True:
        print('1. Cadastrar usuário')
        print('2. Locar Livro')


        opcao=input('Escolha uma opção:')

        if opcao in menus:
            funcao_escolhida=menus[opcao]
            funcao_escolhida(sistema)
        else:
            print('Escolha opções que estão dentro do menu.')
