import os
from pathlib import Path
from sqlite3 import Cursor

import _mysql_connector
from dotenv import load_dotenv
import mysql
import mysql.connector

load_dotenv(path(__file__).with_name(".env"))

def executar_sql(sql, parametros=()):
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    Cursor = None

    try: 
        cursor = conexao.cursor(Dictionary=True)
        cursor.execute(sql, parametros)
        return cursor.fetchall()
    finally:
        if cursor is not None:
            cursor.close()
        conexao.close()