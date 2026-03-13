from banco.conexao import conectar
from modelos.emprestimo import Emprestimo

class Repositorio_Emprestimos():

    def registrar_emprestimo_SQL(self, id_usuario, id_livro):
        conn = conectar()
        cursor = conn.cursor()


        cursor.execute("INSERT INTO emprestimos(id_usuario, id_livro) VALUES (?,?)", (id_usuario, id_livro))
        conn.commit()
        conn.close()

    def buscar_emprestimo_por_id_livro_SQL(self, id_livro):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM emprestimos WHERE id_livro = ?", (id_livro, ))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            emprestimo_objeto_encontrado = Emprestimo(dado['id_livro'], dado['id_usuario'], dado['status'], dado['id_emprestimos'])
            return emprestimo_objeto_encontrado
        
        return 'Livro sem contrato de locação ativo no sistema.'
    
    def buscar_emprestimo_por_id_usuario_SQL(self, id_usuario):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM emprestimos WHERE id_usuario = ?", (id_usuario, ))
        dados = cursor.fetchall()
        conn.close

        if dados:
            emprestimo_objeto_encontrado = Emprestimo(dados['id_livro'], dados['id_usuario'], dados['status'], dados['id_emprestimos'])
            return emprestimo_objeto_encontrado
        
        return 'Usuário sem contrato de locação ativo no sistema.'

    def listar_todos_emprestimos_SQL (self):
        conn = conectar()
        cursor = conn.cursor()
        acervo_objetos_emprestimos = []

        cursor.execute("SELECT * FROM emprestimos")
        dados = cursor.fetchall()
        conn.close()

        if dados:
            for emprestimo in dados:
                emprestimo_objeto = Emprestimo(emprestimo['id_livro'], emprestimo['id_usuario'], emprestimo['status'])
                acervo_objetos_emprestimos.append(emprestimo_objeto)

            return acervo_objetos_emprestimos

        return 'Sem contratos de locação no sistema.'
    
    def deletar_emprestimo_SQL(self, id_emprestimos):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM emprestimos WHERE id_emprestimos = ?", (id_emprestimos, ))
        conn.commit()
        conn.close()
