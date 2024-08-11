import sqlite3 as sql 

def db_conn():
    conn = sql.connect("Banco_inu.db")
    cursor = conn.cursor()
    return conn, cursor
    
def criar_table():
    conn, cursor = db_conn()
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpf TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT  NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS DadosUsuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER, 
        nome TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT  NULL,
        sobrenome TEXT UNIQUE NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        cep TEXT UNIQUE NOT NULL,
        nome_pai TEXT UNIQUE NOT NULL,
        nome_mae TEXT UNIQUE NOT NULL,
        países TEXT UNIQUE NOT NULL,
        Am TEXT UNIQUE NOT NULL,
        cidade TEXT UNIQUE NOT NULL,
        data_nascimento TEXT UNIQUE NOT NULL,  
        teleone TEXT UNIQUE NOT NULL,
        data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )""")
    
    
    
    cursor.execute(""" CREATE TABLE IF NOT EXISTS  HistoriocoBancario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        Salto_do_dia TEXT,
        extrado TEXT,
        descricao TEXT,
        data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )""")
    
    conn.commit()
    conn.close()
    
criar_table()