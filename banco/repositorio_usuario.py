from banco.conexao import conectar
from modelos.usuario import Usuario

class Repositorio_Usuario():
    
    def cadastrar_usuario_SQL (self, nome, telefone):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO usuarios(nome, telefone) VALUES(?,?)", (nome, telefone))
        conn.commit()
        conn.close()

    def listar_usuarios_SQL (self):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()
        conn.close()
        acervo_objetos_usuarios = []

        if dados:
            for usuario in dados:
                usuario_objeto = Usuario(usuario["nome"], usuario["telefone"], usuario["id_usuario"])
                acervo_objetos_usuarios.append(usuario_objeto)
                
        return acervo_objetos_usuarios
            
    def buscar_usuario_por_id_SQL (self, id_usuario_pesquisado):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = ?", (id_usuario_pesquisado, ))
        dado = cursor.fetchone()
        conn.close()

        if dado:
            usuario_objeto_encontrado = Usuario(dado['nome'], dado['telefone'], dado['id_usuario'])

            return usuario_objeto_encontrado
    
        return 'Usuário não encontrado no sistema!'
    
    def deletar_usuario_por_id_SQL (self, id_usuario_deletar):
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM usuarios WHERE id_usuario = ?", (id_usuario_deletar, ))
        conn.commit()
        conn.close()