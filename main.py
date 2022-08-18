import pyodbc


dados_conexao = ("Driver={SQLite3 ODBC Driver};", "Server=localhost;", "Database=Estoque.db;")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()











from window import *


