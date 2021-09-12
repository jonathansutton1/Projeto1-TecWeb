import sqlite3
from dataclasses import dataclass

class Database:
    def __init__(self,bdd):
        self.conn = sqlite3.connect(bdd+".db")
        self.criatabela = "CREATE TABLE IF NOT EXISTS dados_pessoais (nome_da_rua TEXT NOT NULL, cpf TEXT NOT NULL UNIQUE, identificador INTEGER PRIMARY KEY);"
        self.conexao.execute(self.criatabela)

    def add(self,note):
        info = "INSERT INTO dados_pessoais (nome_da_rua,cpf) VALUES ('R. Quatá','123.456.789-00');"
        self.conn.execute(info).commit()




@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''