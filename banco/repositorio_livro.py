from banco.conexao import conectar
from modelos.livro import Livro

class Repositorio_Livro():

    def cadastrar_livro_SQL (self, titulo, autor, ano):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO livros(titulo, autor, ano, disponivel) VALUES (?,?,?,1)", (titulo, autor, ano))
        conn.commit()
        conn.close()

    def listar_livros_SQL (self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM livros")
        dados = cursor.fetchall()
        conn.close()
        acervo_objetos_livros = []
        if dados:
            for livro in dados:
                livro_objeto  = Livro(livro['id_livro'], livro['titulo'], livro['autor'], livro['ano'], livro['disponivel'])
                acervo_objetos_livros.append(livro_objeto )

            return acervo_objetos_livros

        return None
    
    def buscar_livro_por_id_SQL (self, id_livro_pesquisado):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM livros WHERE id_livro = ?", (id_livro_pesquisado, ))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            livro_objeto_encontrado = Livro(dado['id_livro'], dado['titulo'], dado['autor'], dado['ano'], dado['disponivel'])
            return livro_objeto_encontrado

        return 'ID do livro não encontrado no sistema.'
    
    def buscar_livro_por_titulo_SQL (self, titulo):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM livros WHERE  LOWER(titulo) = LOWER(?) ", (titulo, ))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            livro_objeto_encontrado = Livro(dado['id_livro'], dado['titulo'], dado['autor'], dado['ano'], dado['disponivel'])
            return livro_objeto_encontrado

        return None
    
    def deletar_livro_id (self, id_livro):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM livros WHERE id_livro = ?"(id_livro, ))
        conn.commit()
        conn.close()

    def mudar_status_livro_SQL (self, novo_status, id_livro):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("UPDATE livros set disponivel = ? WHERE id_livro=?", (novo_status, id_livro))
        conn.commit()
        conn.close()