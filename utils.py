import _sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_NAME = 'minha_db.sqlite3'
DB_PATH = BASE_DIR / DB_NAME
TABLE_NAME = 'itensComprados'

def conectar_db():
    conexao = _sqlite3.connect(DB_PATH)
    return conexao

def definir_tabela():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            preco REAL NOT NULL
        );
    ''')
    conexao.commit()
    cursor.close()
    conexao.close()

def inserir_dados(nome, preco):
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(f'''
        INSERT INTO {TABLE_NAME} (name, preco) VALUES (?, ?);
    ''', (nome, preco))
    conexao.commit()
    cursor.close()
    conexao.close()

def deleter_dados(nome):
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(f'''
        DELETE FROM {TABLE_NAME} WHERE name = ?;
    ''', (nome,))
    conexao.commit()
    cursor.close()
    conexao.close()

def atualizar_preco(nome, novo_preco):
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(f'''
        UPDATE {TABLE_NAME} SET preco = ? WHERE name = ?;
    ''', (novo_preco, nome))
    conexao.commit()
    cursor.close()
    conexao.close()

def listar_itens():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute(f'''
        SELECT * FROM {TABLE_NAME};
    ''')
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)