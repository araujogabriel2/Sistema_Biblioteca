import sqlite3

def conectar():
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row
    return conn 

conn = conectar()
cursor = conn.cursor()

#tabela usuarios
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios(
        id_usuario INTEGER PRIMARY KEY,
        nome TEXT,
        telefone TEXT
    )
    """)

#tabela livros 
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS livros(
        id_livro INTEGER PRIMARY KEY,
        titulo TEXT,
        autor TEXT,
        ano INTEGER,
        disponivel INTEGER
    )
    """)

#tabela emprestimos
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS emprestimos(
        id_emprestimos INTEGER PRIMARY KEY, 
        id_usuario INTEGER, 
        id_livro INTEGER,
        status INTEGER, 
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
        FOREIGN KEY(id_livro) REFERENCES livros (id_livro)
    )
    """)