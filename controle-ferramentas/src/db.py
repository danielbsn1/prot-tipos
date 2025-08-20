import sqlite3

def criar_banco():
    conn = sqlite3.connect("ferramentas.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ferramentas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            codigo TEXT UNIQUE NOT NULL,
            categoria TEXT,
            localizacao TEXT,
            responsavel TEXT,
            data_aquisicao TEXT,
            situacao TEXT
        );
    """)

    conn.commit()
    conn.close()