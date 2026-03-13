from banco.repositorio_livro import  Repositorio_Livro
from banco.repositorio_usuario import Repositorio_Usuario
from banco.repositorio_emprestimos import Repositorio_Emprestimos



class Biblioteca:
    def __init__(self):
        self.repositoriousuario= Repositorio_Usuario()
        self.repositoriolivro = Repositorio_Livro()
        self.repositorioemprestimo = Repositorio_Emprestimos()
        
    # FUNÇÕES USUÁRIO
    def cadastrar_usuario(self, nome, telefone):
        self.repositoriousuario.cadastrar_usuario_SQL (nome, telefone)
        return f'{nome} cadastrado com sucesso!'
    
    def buscar_usuario_id(self, id_usuario ):
        return self.repositoriousuario.buscar_usuario_por_id_SQL(id_usuario)
    
    def listar_usuarios(self):
        return self.repositoriousuario.listar_usuarios_SQL()
    
    def deletar_usuario(self, id_usuario):
        usuario_encontrado = self.buscar_usuario_id(id_usuario)

        if usuario_encontrado:
            nome = usuario_encontrado.nome
            self.repositoriousuario.deletar_usuario_por_id_SQL(id_usuario)
            return f'O usuário {nome} foi deletado com sucesso!'
        return None
    
    # FUNÇÕES LIVRO
    def cadastrar_livro(self, titulo, autor, ano):
        livro = self.repositoriolivro.buscar_livro_por_titulo_SQL(titulo)
        if livro:
            return "Livro já cadastrado!"
        self.repositoriolivro.cadastrar_livro_SQL(titulo, autor, ano)
        return f'{titulo} cadastrado com sucesso!'
    
    def buscar_livro_id(self, id_livro):
        return self.repositoriolivro.buscar_livro_por_id_SQL(id_livro)

    def listar_livros(self):
        return self.repositoriolivro.listar_livros_SQL()
    
    def deletar_livro(self, id_livro):
        livro_encontrado = self.buscar_livro_por_id(id_livro)

        if livro_encontrado:
            nome = livro_encontrado.titulo
            self.repositoriolivro.deletar_livro_id (id_livro)
            return f'O livro {nome} foi deletado com sucesso!'
        return None

    # FERRAMENTAS DE EMPRESTIMO
    def registrar_emprestimo(self, id_usuario, id_livro):
        return self.repositorioemprestimo.registrar_emprestimo_SQL(id_usuario, id_livro)
    
    def buscar_emprestimo_id_livro(self, id_emprestimo):
        return self.repositorioemprestimo.buscar_emprestimo_por_id_livro_SQL(id_emprestimo)
    
    def buscar_emprestimo_id_usuario(self, id_usuario):
        return self.repositorioemprestimo.buscar_emprestimo_por_id_usuario_SQL(id_usuario)
    
    def listar_emprestimos(self):
        return self.repositorioemprestimo.listar_todos_emprestimos_SQL()
    
    def deletar_emprestimo(self, id_emprestimo):
        return self.repositorioemprestimo.deletar_emprestimo_SQL(id_emprestimo)
    
    # EMPRESTIMO 
    def alugar_livro(self, id_usuario, id_livro):
        usuario = self.buscar_usuario_id(id_usuario)
        livro = self.buscar_livro_id(id_livro)

        if not usuario:
            return 'Usuário não encontrado!'
        if not livro:
            return 'Livro não encontrado!'
        if livro.disponivel == 0:
            return f'Livro {livro.titulo} não está disponível!'
        
        self.repositorioemprestimo.registrar_emprestimo_SQL(id_usuario, id_livro)
        self.repositoriolivro.mudar_status_livro_SQL(0, id_livro)
        emprestimo = self.repositorioemprestimo.buscar_emprestimo_por_id_livro_SQL(id_livro)


        return f"""
                ----------- ALUGADO COM SUCESSO -----------

                LIVRO: {livro.titulo} 
                NOME: {usuario.nome}
                TEL: {usuario.telefone}
                ID EMPRESTIMO: {emprestimo.id_emprestimos}
                """
    
    def devolver_livro(self, id_livro):
        emprestimo = self.repositorioemprestimo.buscar_emprestimo_por_id_livro_SQL(id_livro)

        if not emprestimo:
            return 'Contrato não encontrado!'
        
        self.repositorioemprestimo.deletar_emprestimo_SQL(emprestimo.id_emprestimos)
        self.repositoriolivro.mudar_status_livro_SQL(1, id_livro)

        return f"""
                ----------- DEVOLVIDO COM SUCESSO -----------

                ID LIVRO: {emprestimo.id_livro}
                ID EMPRESTIMO: {emprestimo.id_emprestimos}
                ID USUÁRIO: {emprestimo.id_usuario}
                """

        
        


        
        

    

       
