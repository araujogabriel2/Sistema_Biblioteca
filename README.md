# Sistema de Gerenciamento de Biblioteca

Um sistema em Python focado em Orientação a Objetos para gerenciar o acervo de uma biblioteca, cadastro de usuários e controle de empréstimos.

##  Sobre o Projeto

Este projeto foi desenvolvido para aplicar conceitos fundamentais de programação, como:
- **POO (Programação Orientada a Objetos):** Classes, Objetos e Atributos.
- **Arquitetura de Software:** Separação de responsabilidades (Modelos, Interface, Dados).
- **Lógica de Programação:** Listas, Dicionários e Laços de Repetição.

O diferencial deste sistema é que ele já inicia com uma carga automática de dados (Seed Data), permitindo testar as funções sem precisar cadastrar tudo do zero.

##  Funcionalidades

-  **Carga Automática:** Carrega 20 livros clássicos automaticamente ao iniciar.
-  **Cadastro de Usuários:** Registro de nome, telefone e geração de ID.
-  **Busca Inteligente:**
  - Pesquisa de livros por Título.
  - Pesquisa de usuários por ID.
-  **Sistema de Locação:** Verifica disponibilidade do livro antes de alugar.
-  **Interface Limpa:** Menus interativos no terminal.

##  Estrutura do Projeto

O código foi organizado para facilitar a manutenção:

├──  modelos/          # As Classes (O molde das coisas: Livro, Usuario, Biblioteca)

├──  interface/        # O Visual (Menus e prints para o usuário)

├──  servicos/         # Regras de negócio extras

├──  dados.py          # Banco de dados inicial (Lista de livros)

└──  main.py           # Arquivo principal que inicia o sistema

##  Tecnologias Utilizadas

- Python 3
- Biblioteca `os` (Para limpeza de terminal)

##  Como Executar

1. Certifique-se de ter o Python instalado.
2. Clone este repositório ou baixe os arquivos.
3. Abra o terminal na pasta do projeto.
4. Execute o comando:

python main.py

## Autor

Desenvolvido por **Gabriel Araújo** durante estudos de Python e POO.
